import pytest

from adventofcode2020.utils import advent_utils


def test_string_to_list_of_ints():
    input_data = "2,4,5, 300,-3,0"
    result = advent_utils.string_to_list_of_ints(input_data)

    assert result == [2, 4, 5, 300, -3, 0]


def test_string_to_list_of_ints_with_dash():
    # Split on a -, does not support negative ints
    input_data = "2-4-5-300-3-0"
    result = advent_utils.string_to_list_of_ints(input_data, "-")

    assert result == [2, 4, 5, 300, 3, 0]


def test_invalid_list_to_list_of_ints():
    input_data = "these,are,not,the,ints,you're,looking,for"
    with pytest.raises(ValueError):
        advent_utils.string_to_list_of_ints(input_data)


def test_string_of_single_to_list_of_ints():
    input_data = "23272930"
    result = advent_utils.string_of_single_to_list_of_ints(input_data)

    assert result == [2, 3, 2, 7, 2, 9, 3, 0]


def test_string_of_invalid_single_to_list_of_ints():
    input_data = "2327-2930"
    with pytest.raises(ValueError):
        advent_utils.string_of_single_to_list_of_ints(input_data)
