import pytest

from adventofcode2020.solutions.day05 import Day05PartA


class TestDay05PartA:
    @pytest.mark.parametrize(
        ("input_data", "row", "col", "seat_nr"),
        [
            ("FBFBBFFRLR", 44, 5, 357),
            ("BFFFBBFRRR", 70, 7, 567),
            ("FFFBBBFRRR", 14, 7, 119),
            ("BBFFBBFRLL", 102, 4, 820),
            ("FFFFFFFRRR", 0, 7, 7),
            ("BBBBBBBLLL", 127, 0, 1016),
        ],
    )
    def test_bin_search(self, input_data: str, row: int, col: int, seat_nr: int):
        solution = Day05PartA()
        calc_row = solution.compute_position_row(input_data)
        assert calc_row == row

        calc_col = solution.compute_position_col(input_data)
        assert calc_col == col

        assert solution.compute_seat_nr(input_data) == seat_nr

    def test_day05a_data(self):
        """ Result we got when we did the real solution """
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res != 807  # Too low
        assert res == 813
