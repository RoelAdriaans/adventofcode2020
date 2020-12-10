import pytest

from adventofcode2020.solutions.day10 import Day10PartB


class TestDay10PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        (
            ([0, 1, 4, 5, 6, 7], 4),
            ([0, 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], 8),
        ),
    )
    def test_day10b_combinations(self, input_data, expected_result):
        solution = Day10PartB()
        result = solution.find_combinations(sorted(input_data))
        assert result == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4\n", 8),
            (
                "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n"
                "38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3\n",
                19208,
            ),
        ],
    )
    def test_day10b_solve(self, input_data, expected_result):
        solution = Day10PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day10b_data(self):
        """ Result we got when we did the real solution """
        solution = Day10PartB()
        res = solution("day_10/day10.txt")
        assert res == 12401793332096
