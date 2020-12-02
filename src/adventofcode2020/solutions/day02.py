import re
from typing import NamedTuple

from adventofcode2020.utils.abstract import FileReaderSolution


class PassPol(NamedTuple):
    at_least: int
    at_most: int
    letter: str
    password: str


class Day02:
    @staticmethod
    def split(input_password) -> PassPol:
        """
        Input `7-9 r: rrrkrrrrrnrrmj`, output is PassPol namedtuple
        """
        results = re.match(r"(\d*)-(\d*) (.): (\w*)", input_password)

        # Make mypy happy
        assert results

        passpol = PassPol(
            at_least=int(results[1]),
            at_most=int(results[2]),
            letter=results[3],
            password=results[4],
        )
        return passpol


class Day02PartA(Day02, FileReaderSolution):
    def validate_passwords(self, policy: PassPol) -> bool:
        """
        Validate that `password` is valid, with the PassPol policy list
        """
        at_least = policy.at_least
        at_most = policy.at_most
        letter = policy.letter

        # `letter` must be `at_least` time in the list, and at most `at_most` times
        counts = policy.password.count(letter)
        if counts < at_least:
            # To little
            return False
        if counts > at_most:
            # To much
            return False
        return True

    def solve(self, input_data: str) -> int:

        password_list = [
            self.split(x.strip()) for x in input_data.split("\n") if len(x.strip()) >= 1
        ]

        results = [self.validate_passwords(policy=x) for x in password_list]
        return sum(results)


class Day02PartB(Day02, FileReaderSolution):
    def validate_passwords(self, policy: PassPol) -> bool:
        """
        Validate that `password` is valid, with the PassPol policy list
        """
        first_char = policy.at_least
        second_char = policy.at_most
        letter = policy.letter

        # `letter` must be at place first_char - 1 and second_char - 1,
        # since it's 1-indexed and not zero indexed
        # Exactly one of these positions must contain the given letter, xor.
        if (policy.password[first_char - 1] == letter) ^ (
            policy.password[second_char - 1] == letter
        ):
            return True
        else:
            return False

    def solve(self, input_data: str) -> int:
        password_list = [
            self.split(x.strip()) for x in input_data.split("\n") if len(x.strip()) >= 1
        ]

        results = [self.validate_passwords(policy=x) for x in password_list]
        return sum(results)
