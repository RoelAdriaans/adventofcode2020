import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

day_name = "{{ cookiecutter.day }}"

# Convert to int:
try:
    int_day_name = int(day_name)
except ValueError:
    print(f"ERROR: day_name: {day_name} is not a valid integer!")
    sys.exit(1)


if not (1 <= int_day_name <= 25):
    print(f"ERROR: day_name: {day_name} is not a valid day, must be between 1 and 25")
    sys.exit(1)

# Check that we have a leading zero when needed:
prefix_day_name = "{:02d}".format(int_day_name)
if prefix_day_name != day_name:
    print(f"ERROR: day_name: {day_name} must have a leading zero")
    sys.exit(1)
