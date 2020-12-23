from adventofcode2020.utils.abstract import FileReaderSolution


class Day13:
    @staticmethod
    def closest(depart_time, bus_id) -> int:
        time = 0
        while True:
            if bus_id + time > depart_time:
                return (time + bus_id) - depart_time
            else:
                time += bus_id


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        depart_time = int(lines[0])
        bus_ids = [int(bus_id) for bus_id in lines[1].split(",") if bus_id != "x"]

        times = {}
        for bus in bus_ids:
            times[bus] = self.closest(depart_time=depart_time, bus_id=bus)

        # key = does not play nice with mypy
        min_bus_id = min(times, key=times.get)  # type: ignore

        return min_bus_id * times[min_bus_id]


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()

        start_times = {}
        for i, value in enumerate(lines[1].split(",")):
            if value != "x":
                start_times[int(value)] = i

        # What happends:
        # Bus 7 : Match every  7 times
        # This means we can increase the step with 7
        # Bus 13: Match every 13 times
        # This means we can increate the step size with 7 * 13
        # Bus 59: Match every 59 times:
        # This means we can increase the stepsize with 7 * 13 * 59
        # We are increasing the steps until we find the right solution
        t, step = 0, 1
        for bus_id, mins in start_times.items():
            # check to see if bus is departing at current time
            while (t + mins) % bus_id != 0:
                t += step
            # increase step multiple to find next min for next bus
            step *= bus_id

        return t
