import os
import unittest
from pathlib import Path

import matplotlib.pyplot as plt
import psutil
from rustworkx.visualization import mpl_draw

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

        plt.figure(figsize=(50, 50))

        # 2. Gọi hàm vẽ của rustworkx như bình thể
        mpl_draw(
            graph._viz_graph,
            with_labels=True,
            labels=lambda x: graph._nodes_names.get(x, str(x)),
            node_color="#1f78b4",
            node_size=1000,
            font_size=10,
            edge_color="gray",
        )

        # 3. Lưu đồ thị ra file ảnh (hỗ trợ .png, .jpg, .svg, .pdf...)
        # bbox_inches='tight' giúp cắt bỏ các khoảng trắng thừa xung quanh ảnh
        plt.savefig(
            "data/northwind-graph.png", format="png", dpi=300, bbox_inches="tight"
        )

        # 4. Xóa khung vẽ hiện tại để giải phóng bộ nhớ (rất quan trọng nếu bạn vẽ nhiều ảnh trong vòng lặp)
        plt.close()

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
