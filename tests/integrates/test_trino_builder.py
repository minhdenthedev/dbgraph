import logging
import unittest
from uuid import uuid4

from dbgraph import SQLGraphBuilder
from dbgraph.entity.aspect import (
    RCategoricalStatistics, RNumericalStatistics,
    RTemporalStatistics,
)
from dbgraph.persistent.orm_graph_persistent import ORMGraphPersistent


class TestTrinoBuilder(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("sqlalchemy").setLevel(
            logging.WARNING,
        )  # ví dụ framework SQLAlchemy
        logging.getLogger("urllib3").setLevel(logging.WARNING)  # ví dụ requests/HTTP

    def setUp(self) -> None:
        self.uri = ("trino://45ba00f2-189d-4215-9eb4-8ad92b5892e6:f4asulq4wluhis651wfi"
                    "@ec29c5d8-5c42-45eb-a9c6-1c594383db6e.idma.cloud:443"
                    "/vnpt_net_cell_clk/app")
        self.builder = SQLGraphBuilder(self.uri, use_tqdm=True)

    def test_table_names(self):
        target = [
            "mca_hourly",
            "fms_daily",
            "relation_mobility_4g_hourly",
            "mentor_hourly",
            "sector_carrier_weekly",
            "mentor_hourly_lte_20260806",
            "cem_daily",
            "danhsach_40k_cell",
            "relation_mobility_2g_hourly",
            "relation_mobility_3g_hourly",
        ]
        table_names = self.builder.table_names
        self.assertEqual(set(target), set(table_names))

    def test__get_table_orm(self):
        orm_table = self.builder._get_table_orm("relation_mobility_4g_hourly")
        self.assertEqual("relation_mobility_4g_hourly", str(orm_table))
        columns = self.builder._get_table_orm("relation_mobility_4g_hourly").columns
        self.assertEqual(11, len(columns))
        for column in columns:
            print(f"{column}: {column.type}")

    def test__get_table_row_count(self):
        row_count = self.builder._get_row_count("mca_hourly")
        self.assertEqual(10268209, row_count)

    def test__get_null_info(self):
        columns = self.builder._get_table_orm("mca_hourly").columns
        target_column = columns[0]
        non_null, null = self.builder._get_null_info(target_column)
        self.assertEqual(10268209, non_null)
        self.assertEqual(0, null)

    def test__get_cat_stats_aspect(self):
        column = self.builder._get_column_orm("fms_daily", "alarm_detail")
        stats_aspect = self.builder._get_stats_aspect(column)
        self.assertIsNone(stats_aspect.categorical_stats)
        self.assertTrue(stats_aspect.is_textual)

    def test__get_numerical_stats_aspect(self):
        column = self.builder._get_column_orm("mca_hourly", "reportstatus")
        num_stats = self.builder._get_numerical_stats_aspect(column)
        self.assertIsInstance(num_stats, RNumericalStatistics)

    def test__get_temp_aspect(self):
        column = self.builder._get_column_orm("mca_hourly", "calltime")
        temp_stats = self.builder._get_temp_aspect(column)
        self.assertIsInstance(temp_stats, RTemporalStatistics)

    def test_build_graph(self):
        graph = self.builder.build_graph()
        print("Saving graph...")
        persistent = ORMGraphPersistent("sqlite:///net_cell_app.db")
        persistent.save_graph(
            uuid4(),
            "net-cell-app",
            graph,
        )

    def test__is_column_textual(self):
        column = self.builder._get_column_orm("fms_daily", "alarm_detail")
        is_textual = self.builder._is_column_textual(column)
        self.assertTrue(is_textual)


if __name__ == '__main__':
    unittest.main()
