from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import Any, Dict, Optional

from adventofcode2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


@dataclass
class Bag:
    """
    A bag has a color, and contains other <n> bags. This is my node.
    """

    color: str
    num_bags: int
    contains: Dict[Bag, int]  # Edge

    def __init__(self, color, num_bags):
        self.color = color
        self.num_bags = num_bags
        self.contains = {}

    def __repr__(self):
        return f"<Bag: {self.color} contains {len(self.contains)} bags>"

    def add_bag(self, bag: Bag, number: int):
        if bag in self.contains:
            raise ValueError(f"Bag {bag=} is already in this bag!")

        self.contains[bag] = number

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Bag):
            return NotImplemented
        return self.color == other.color

    def __hash__(self):
        return hash(self.color)


class Day07:
    def __init__(self):
        self.bags: Dict[str, Bag] = {}
        self.root_bag: Optional[Bag] = None

    def from_string(self, input_str: str) -> Bag:
        """
        Return a bag with contents:

        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dark tan bags contain 4 faded white bags.
        """

        color_regex = r"^([\w\s]+) bags contain ([\w\s,]+)"
        color_match = re.match(color_regex, input_str)
        assert color_match

        color = color_match[1]

        logger.debug(f"Root bag with {color=}")
        root_bag = Bag(color, 1)

        # See if we have any bags in our bag
        contents = [bag.strip() for bag in color_match[2].split(",")]

        for child_bag in contents:
            # Remove bag and bags
            child_bag = child_bag.replace("bags", "").replace("bag", "").strip()
            content_regex = r"^([\d]+) ([\w\s]+)$"
            child_match = re.match(content_regex, child_bag)
            if child_match is None:
                # No bags in this bag
                continue

            number = int(child_match[1])
            child_color = child_match[2]
            child_bag_inst = Bag(child_color, number)
            root_bag.add_bag(child_bag_inst, number)

        # Append root bag to our bags
        self.bags[color] = root_bag
        return root_bag

    def find_bag(self, color="shiny gold") -> int:
        num = []
        for bag in self.bags.values():
            if bag.color == color:
                # We cannot ourselves,
                continue
            res = self.resolve_tree(bag, color)
            num.append(res)

            logger.info(f"{bag.color=} can hold: {res=}")

        return sum(num)

    def resolve_tree(self, bag: Bag, color) -> bool:
        if bag.color == color:
            return True
        does_contain_color = any(
            [
                self.resolve_tree(self.bags[child_bag.color], color)
                for child_bag in bag.contains
            ]
        )
        return does_contain_color

    def count_bags_for_color(self, color="shiny gold") -> int:
        cnt = 1
        for sub_bag in self.bags[color].contains:
            # How many times does current sub_bag contain bag?
            cnt += self.count_bags_for_color(sub_bag.color) * sub_bag.num_bags
        return cnt


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        for bag_line in input_data.splitlines():
            self.from_string(bag_line)

        # Now we should have all the bags?
        # Count how many bags can make
        res = self.find_bag()
        return res


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        for bag_line in input_data.splitlines():
            self.from_string(bag_line)

        # Find out how many bags we need to take with us
        # And subtract one for the shiny gold one
        res = self.count_bags_for_color("shiny gold") - 1
        return res
