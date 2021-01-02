import pytest

from adventofcode2020.solutions.day14 import Day14PartB


class TestDay14PartB:
    @pytest.mark.parametrize(
        ("address", "input_mask", "possible_addresses"),
        [
            (
                42,
                "000000000000000000000000000000X1001X",
                [
                    "000000000000000000000000000000011010",
                    "000000000000000000000000000000011011",
                    "000000000000000000000000000000111010",
                    "000000000000000000000000000000111011",
                ],
            ),
            (
                26,
                "00000000000000000000000000000000X0XX",
                [
                    "000000000000000000000000000000010000",
                    "000000000000000000000000000000010001",
                    "000000000000000000000000000000010010",
                    "000000000000000000000000000000010011",
                    "000000000000000000000000000000011000",
                    "000000000000000000000000000000011001",
                    "000000000000000000000000000000011010",
                    "000000000000000000000000000000011011",
                ],
            ),
        ],
    )
    def test_day16b_mask_to_addresses(self, address, input_mask, possible_addresses):
        solution = Day14PartB()
        result = solution.mask_to_addresses(address=address, mask=input_mask)
        assert len(result) == len(possible_addresses)
        # Convert the possible addresses to integers
        int_addresses = [int(x, 2) for x in possible_addresses]
        for res in result:
            assert res in int_addresses

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                [
                    "mask = 000000000000000000000000000000X1001X",
                    "mem[42] = 100",
                    "mask = 00000000000000000000000000000000X0XX",
                    "mem[26] = 1",
                ],
                208,
            )
        ],
    )
    def test_day14b_solve(self, input_data, expected_result):
        input_data = "\n".join(input_data)
        solution = Day14PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day14b_data(self):
        """ Result we got when we did the real solution """
        solution = Day14PartB()
        res = solution("day_14/day14.txt")
        assert res == 4254673508445
