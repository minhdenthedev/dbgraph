import os
import unittest

import psutil

from dbgraph.builder.sql_graph_builder import SQLGraphBuilder
from dbgraph.entity.link_type import LinkType


def get_kv_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


class TestSQLGraphBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_builder = SQLGraphBuilder("sqlite:///data/northwind.db")

    def test_build_graph(self):
        from time import perf_counter_ns

        from pympler import asizeof

        mem_before = get_kv_memory()

        start = perf_counter_ns()

        graph = self.graph_builder.build_graph()

        end = perf_counter_ns()
        print(f"Duration: {(end - start) / 1000000000}s")

        mem_after = get_kv_memory()

        mem_used = mem_after - mem_before
        graph_size = asizeof.asizeof(graph)
        print(f"Dung lượng graph theo MB: {graph_size / (1024 * 1024):.2f} MB")
        print(f"Hàm build_graph tốn thêm: {mem_used / (1024 * 1024):.2f} MB RAM")
        self.assertTrue(False)

    def test__build_links(self):
        _ = self.graph_builder._build_assets()
        links = self.graph_builder._build_links()
        for link in links:
            if link.type == LinkType.FOREIGN_KEY:
                print(link)
        self.assertEqual(len(links), 101)
        self.assertTrue(False)

    def test__build_assets(self):
        assets = self.graph_builder._build_assets()
        for asset in assets:
            print(asset)
        self.assertTrue(False)

    def test__get_tables_names(self):
        tables = self.graph_builder.table_names
        print(tables)
        self.assertFalse(True)

    def test__get_table_nrows(self):
        nrow = self.graph_builder._get_table_nrows("Orders")
        print(nrow)
        self.assertFalse(True)

    def test__get_columns_assets(self):
        assets = self.graph_builder._get_columns_assets("Orders")
        for asset in assets:
            print(asset)
        self.assertTrue(False)

    def test__get_fk_links(self):
        self.graph_builder._build_fk_links()
        self.assertTrue(False)

    def test__orm_tables(self):
        orm_tables = self.graph_builder._orm_tables
        print(orm_tables)
        self.assertTrue(False)

    def test__table_schema(self):
        schema = self.graph_builder._get_table_schema_aspect("Orders")
        print(schema)
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
