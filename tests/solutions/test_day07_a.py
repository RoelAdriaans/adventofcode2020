import pytest

from adventofcode2020.solutions.day07 import Day07PartA


class TestDay07PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result", "bag_color"),
        [
            (
                "light red bags contain 1 bright white bag, 2 muted yellow bags",
                2,
                "light red",
            ),
            ("faded blue bags contain no other bags.", 0, "faded blue"),
            ("dark tan bags contain 4 faded white bags.", 1, "dark tan"),
            (
                "dull turquoise bags contain 2 plaid olive bags, "
                "5 striped turquoise bags, 5 muted brown bags, 1 vibrant magenta bag.",
                4,
                "dull turquoise",
            ),
        ],
    )
    def test_day07_from_string(self, input_data, expected_result, bag_color):
        solution = Day07PartA()
        bag = solution.from_string(input_data)
        # Check how many bags the bag contains
        assert len(bag.contains) == expected_result
        assert bag.color == bag_color

    def test_day07a_solve(self):
        test_input = "\n".join(
            [
                "light red bags contain 1 bright white bag, 2 muted yellow bags.",
                "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                "bright white bags contain 1 shiny gold bag.",
                "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                "faded blue bags contain no other bags.",
                "dotted black bags contain no other bags.",
            ]
        )

        solution = Day07PartA()
        result = solution.solve(test_input)
        assert result == 4

    def test_day07a_data(self):
        """ Result we got when we did the real solution """
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 151
