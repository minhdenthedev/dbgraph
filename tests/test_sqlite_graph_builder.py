import os
import unittest
from pathlib import Path

import psutil

from dbgraph.builder.sqlite.sqlite_graph_builder import SQLiteGraphBuilder


def get_kv_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


class TestSQLiteGraphBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_builder = SQLiteGraphBuilder(Path("data/northwind.db"))

    def test_build_graph(self):
        from pympler import asizeof

        mem_before = get_kv_memory()

        graph = self.graph_builder.build_graph()

        mem_after = get_kv_memory()

        mem_used = mem_after - mem_before
        graph_size = asizeof.asizeof(graph)
        print(f"Dung lượng graph theo MB: {graph_size / (1024 * 1024):.2f} MB")
        print(f"Hàm build_graph tốn thêm: {mem_used / (1024 * 1024):.2f} MB RAM")
        md = graph.to_markdown()
        self.assertIsInstance(md, str)
        print(md)

    def test__build_links(self):
        _ = self.graph_builder._build_assets()
        links = self.graph_builder._build_links()
        self.assertEqual(len(links), 101)

    def test__build_assets(self):
        assets = self.graph_builder._build_assets()
        self.assertEqual(len(assets), 101)

    def test__get_tables_names(self):
        tables = self.graph_builder._get_tables_names()
        self.assertEqual(
            tables,
            [
                "Categories",
                "CustomerCustomerDemo",
                "CustomerDemographics",
                "Customers",
                "Employees",
                "EmployeeTerritories",
                "Order Details",
                "Orders",
                "Products",
                "Regions",
                "Shippers",
                "Suppliers",
                "Territories",
            ],
        )


if __name__ == "__main__":
    unittest.main()
