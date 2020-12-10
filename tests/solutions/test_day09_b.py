from adventofcode2020.solutions.day09 import Day09PartB


class TestDay09PartB:
    def test_day09b_solve(self):
        # fmt: off
        integers = [
            35, 20, 15, 25, 47, 40, 62, 55,
            65, 95, 102, 117, 150, 182, 127,
            219, 299, 277, 309, 576
        ]
        # fmt: on

        solution = Day09PartB()
        result = solution.find_slice(integers, 127)
        assert result == 62

    def test_day09b_data(self):
        """ Result we got when we did the real solution """
        solution = Day09PartB()
        res = solution("day_09/day09.txt")
        assert res == 238243506
