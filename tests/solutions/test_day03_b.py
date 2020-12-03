from adventofcode2020.solutions.day03 import Day03PartB


class TestDay03PartB:
    def test_day03b_data(self):
        """ Result we got when we did the real solution """
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res != 294
        assert res != 13163297103
        assert res == 7540141059
