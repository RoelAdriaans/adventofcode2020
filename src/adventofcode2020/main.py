import importlib
import logging
import sys
import timeit

import click
import tqdm

logger = logging.getLogger(__name__)


@click.command()
@click.argument(
    "day",
    type=click.IntRange(1, 25),
)
@click.option("--parta", "part", flag_value="parta")
@click.option("--partb", "part", flag_value="partb")
@click.option(
    "-t",
    "--timeit",
    "timeit_",
    type=click.INT,
    help="Test the solution using timeit with timeit iterations",
)
@click.option("-v", "--verbose", is_flag=True)
def main(day, part, timeit_, verbose):
    """
    Simple program that runs a module from the advent of code.
    DAY is an integer representing the day (1 - 25) that runs that day.
    """
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )

    day = f"{int(day):02}"

    print(
        f"Welcome to Advent of Code 2020 - {day=} - {part=} - {timeit_=} - {verbose=}"
    )

    # Try to import the solution
    import_path = f"adventofcode2020.solutions.day{day}"
    data_path = f"day_{day}/day{day}.txt"

    logger.debug(f"Importing {import_path}")

    try:
        day_module = importlib.import_module(import_path)
    except ModuleNotFoundError:
        print(f"Module {day} is not yet available")
        sys.exit(-65)
    if timeit_:
        execution_times = []
        results = ""

        for _ in tqdm.trange(timeit_):
            time_prior = timeit.default_timer()

            results = run_day(data_path, day, day_module, part)

            time_after = timeit.default_timer()
            execution_times.append(time_after - time_prior)

        average_time = sum(execution_times) / len(execution_times)

        print("Results:")
        print(results)
        print(
            f"Average running time: {average_time:.6f} seconds ({timeit_} iterations)"
        )
    else:
        print("Results:")
        print(run_day(data_path, day, day_module, part))


def run_day(data_path, day, day_module, part):
    if part == "parta":
        return run_parta(data_path, day, day_module)

    elif part == "partb":
        return run_partb(data_path, day, day_module)

    else:
        a = run_parta(data_path, day, day_module)
        b = run_partb(data_path, day, day_module)

        return f"Part A:\n{a}\n\nPart B:\n{b}\n"


def run_parta(data_path, day, day_module):
    result = getattr(day_module, f"Day{day}PartA")()(data_path)
    return result


def run_partb(data_path, day, day_module):
    result = getattr(day_module, f"Day{day}PartB")()(data_path)
    return result


if __name__ == "__main__":
    main()
