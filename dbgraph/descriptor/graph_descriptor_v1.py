import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass

from tqdm import tqdm

from dbgraph.descriptor.graph_descriptor import GraphDescriptor
from dbgraph.entity.aspect import SemanticAspect
from dbgraph.entity.asset import Asset
from dbgraph.entity.rdbgraph import RDatabaseGraph
from dbgraph.llm.llm import LLM


@dataclass
class GraphDescriptorV1(GraphDescriptor):
    """Implementation of Graph Descriptor"""

    llm: LLM
    system_prompt: str
    target_prompt: str
    formating_prompt: str
    max_worker: int = 10

    def _generate_semantic_aspects(
        self, system_prompt: str, user_prompt: str, assets_ids: list[str]
    ) -> dict[str, SemanticAspect]:
        s = self.llm.generate(system_prompt, user_prompt)
        data = json.loads(s) if s else {}
        parsed = {
            k: SemanticAspect(
                name=f"{name}_semantic",
                description=v["description"],
                keywords=v["keywords"],
            )
            for k, (name, v) in zip(assets_ids, data.items())
        }
        return parsed

    def _rbuild_prompt_for_target_asset(
        self, target_asset: Asset, column_assets: list[Asset]
    ) -> str:
        columns_str = [f"- {c.name}" for c in column_assets]
        return self.target_prompt.format(
            asset_type=target_asset.type,
            asset_name=target_asset.name,
            columns_str="\n".join(columns_str),
        )

    def _rbuild_context_for_sub_graph(self, sub_graph: RDatabaseGraph) -> str:
        """Build system prompt to generate semantic aspect for an targeted asset, given the contexts (subgraph)"""
        return self.system_prompt + "\n" + sub_graph.to_markdown()

    def _gather_semantic_aspects(
        self,
        system_prompts: list[str],
        user_prompts: list[str],
        assets_ids_list: list[list[str]],
    ) -> dict[str, SemanticAspect]:
        prompt_pairs = list(zip(system_prompts, user_prompts, assets_ids_list))

        results = {}
        with ThreadPoolExecutor(max_workers=self.max_worker) as executor:
            futures = [
                executor.submit(
                    self._generate_semantic_aspects, pair[0], pair[1], pair[2]
                )
                for pair in prompt_pairs
            ]
            for future in tqdm(
                as_completed(futures),
                total=len(futures),
                desc="Generating asset's semantic aspects",
            ):
                result = future.result()

                results.update(result)
        return results

    def rfill_semantic_aspects(self, graph: RDatabaseGraph) -> RDatabaseGraph:
        tables = graph.get_tables()
        subgraphs = [graph.get_refs_with_columns(table.asset_id) for table in tables]
        columns_lists = [
            [a for a in subgraph.get_columns(table.asset_id)]
            for table, subgraph in zip(tables, subgraphs)
        ]
        system_prompts = [
            self._rbuild_context_for_sub_graph(subgraph) + "\n" + self.formating_prompt
            for subgraph in subgraphs
        ]
        user_prompts = [
            self._rbuild_prompt_for_target_asset(table, columns)
            for table, columns in zip(tables, columns_lists)
        ]
        assets_ids_list = [
            [table.asset_id] + [c.asset_id for c in columns]
            for table, columns in zip(tables, columns_lists)
        ]

        semantic_aspects = self._gather_semantic_aspects(
            system_prompts, user_prompts, assets_ids_list
        )
        for k, aspect in semantic_aspects.items():
            graph._nodes_data[graph._nodes_idx[k]].aspects["semantic_properties"] = (
                aspect
            )
        return graph
