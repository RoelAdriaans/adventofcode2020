import re
from enum import Enum

from adventofcode2020.utils.abstract import FileReaderSolution


class RequiredFields(Enum):

    byr = "Birth Year"
    iyr = "Issue Year"
    eyr = "Expiration Year"
    hgt = "Height"
    hcl = "Hair Color"
    ecl = "Eye Color"
    pid = "Passport ID"
    cid = "Country ID"

    @staticmethod
    def validate(code, value):
        if code != "cid" and value is None:
            return False

        if code == "byr":
            return 1920 <= int(value) <= 2002
        if code == "iyr":
            return 2010 <= int(value) <= 2020
        if code == "eyr":
            return 2020 <= int(value) <= 2030

        if code == "hgt":
            # hgt:179cm
            unit = value[-2:]
            hgt = int(value[:-2])
            if unit == "cm":
                return 150 <= hgt <= 193
            if unit == "in":
                return 59 <= hgt <= 76
            return False

        if code == "hcl":
            regex = r"^(#)([a-z0-9]){6}$"
            return re.match(pattern=regex, string=value)

        if code == "ecl":
            return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

        if code == "pid":
            regex = r"^([0-9]){9}$"
            return re.match(pattern=regex, string=value)

        if code == "cid":
            return True

        raise ValueError(f"Unknown Code {code}")


class Day04:
    @staticmethod
    def validate_passport(
        passport_lines, requiredfields, skip=None, validate: bool = False
    ) -> bool:
        if skip is None:
            skip = []
        single_line = " ".join([line for line in passport_lines])

        parts = {}
        for field in single_line.split(" "):
            k, v = field.split(":")
            parts[k] = v

        for field_to_check in requiredfields:
            if validate:
                if not RequiredFields.validate(
                    field_to_check.name, parts.get(field_to_check.name, None)
                ):
                    return False
            if field_to_check.name not in parts.keys():
                if field_to_check.name in skip:
                    continue
                else:
                    return False
        return True


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        passport_lines = []
        counts = []
        for line in input_data.splitlines():
            if line:
                passport_lines.append(line)
            else:
                counts.append(
                    self.validate_passport(
                        passport_lines,
                        RequiredFields,
                        skip=["cid"],
                    )
                )
                passport_lines = []
        # And process the last line
        counts.append(
            self.validate_passport(
                passport_lines,
                RequiredFields,
                skip=["cid"],
            )
        )

        return sum(counts)


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        passport_lines = []
        counts = []
        for line in input_data.splitlines():
            if line:
                passport_lines.append(line)
            else:
                counts.append(
                    self.validate_passport(
                        passport_lines, RequiredFields, skip=["cid"], validate=True
                    )
                )
                passport_lines = []
        # And process the last line
        counts.append(
            self.validate_passport(
                passport_lines, RequiredFields, skip=["cid"], validate=True
            )
        )
        return sum(counts)
