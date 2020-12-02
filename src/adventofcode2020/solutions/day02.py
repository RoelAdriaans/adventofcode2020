from adventofcode2020.utils.abstract import FileReaderSolution
from typing import NamedTuple, List
import re


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
        passpol = PassPol(
            at_least=int(results[1]),
            at_most=int(results[2]),
            letter=results[3],
            password=results[4],
        )
        return passpol

    def validate_passwords(self, policy: PassPol) -> bool:
        """
        Validate that `password` is valid, with the PassPol policy list
        """

        at_least = policy.at_least
        at_most = policy.at_most
        letter = policy.letter
        # `letter` must be `at_least` time in the list, and at most `at_moast` times
        counts = policy.password.count(letter)
        if counts < at_least:
            # To little
            return False
        if counts > at_most:
            # To much
            return False
        return True


class Day02PartA(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:

        password_list = [
            self.split(x.strip()) for x in input_data.split("\n") if len(x.strip()) >= 1
        ]

        results = [self.validate_passwords(policy=x) for x in password_list]
        return sum(results)


class Day02PartB(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
