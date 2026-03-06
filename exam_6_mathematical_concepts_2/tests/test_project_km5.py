import unittest
from project_km5 import *


class TestProjectKM5(unittest.TestCase):
    def test_breakeven_point(self):
        # Parallel lines: no breakeven
        self.assertIs(
            breakeven_point((100, 10), (200, 10)),
            -1,
        )

        # Breakeven at 20 units
        self.assertAlmostEqual(
            breakeven_point((50, 5), (100, 3)),
            25.0,
        )

        # Negative slope breakeven
        self.assertAlmostEqual(
            breakeven_point((300, 15), (100, 5)),
            -20.0,
        )

        self.assertAlmostEqual(
            breakeven_point((0, 2), (45000, -1)),
            15000,
        )

    def test_net_flow_accumulation(self):
        # Simple increasing flow
        self.assertAlmostEqual(
            net_flow_accumulation([2, 3, 4], 0, 2),
            19.333333333333332,
        )

        # Flow with negative values
        self.assertAlmostEqual(
            net_flow_accumulation([50, -20, 5], 1, 3),
            363.33333333333337,
        ) 


if __name__ == "__main__":
    unittest.main()
