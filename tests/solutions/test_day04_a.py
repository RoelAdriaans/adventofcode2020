import pytest

from adventofcode2020.solutions.day04 import Day04PartA


class Testday04PartA:
    def test_day04a_solve(self):
        input_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
        solution = Day04PartA()
        result = solution.solve(input_data)
        assert result == 2

    def test_day04a_data(self):
        """ Result we got when we did the real solution """
        solution = Day04PartA()
        res = solution("day_04/day04.txt")
        assert res == 216
