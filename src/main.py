from typing import Tuple

import click

from solutions import day01

modules = [
    (day01.Day01PartA, ("day_01/day01.txt",)),
    (day01.Day01PartB, ("day_01/day01.txt",)),
]


@click.command()
@click.option(
    "--module", type=click.Choice([i[0].__name__ for i in modules]), required=True
)
def main(module):
    """
    Simple program that runs a module from the advent of code
    """
    item = [item for item in modules if item[0].__name__ == module]
    if not item:
        print(f"Module {module} not found")
        return False
    else:
        found_item: Tuple = item[0]

    print(f"Running module '{found_item[0].__name__}'")

    for filename in found_item[1]:
        class_to_run = found_item[0]
        class_instance = class_to_run()
        res = class_instance(filename)
        print(f"Result for {filename}:\n{res}")


if __name__ == "__main__":
    main()
