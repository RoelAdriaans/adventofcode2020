from adventofcode2020.utils.abstract import FileReaderSolution


class Day05:
    @staticmethod
    def compute_position_row(input_str: str) -> int:
        """ Compute binary string to place in the plane, compute the row"""
        hi = 128
        lo = 0
        for x in input_str[:6]:
            total = hi + lo
            if x == "F":
                # Lower half
                hi = int(total / 2)
            else:
                # higher half
                lo = int(total / 2)

        if input_str[6] == "F":
            return lo
        else:
            return hi - 1

    @staticmethod
    def compute_position_col(input_str: str) -> int:
        """ Compute binary string to place in the plane, compute the column """
        hi = 8
        lo = 0
        for x in input_str[-3:]:
            total = hi + lo
            if x == "L":
                # Lower half
                hi = int(total / 2)
            else:
                # higher half
                lo = int(total / 2)

        if input_str[7] == "R":
            return hi - 1
        else:
            return lo

    def compute_seat_nr(self, input_str: str) -> int:
        col = self.compute_position_col(input_str)
        row = self.compute_position_row(input_str)
        res = row * 8 + col
        print(f"{input_str} = {res} ({row=} {col=})")
        return res


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return max(self.compute_seat_nr(x) for x in input_data.splitlines())


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
