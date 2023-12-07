# Your calculation isn't quite right. It looks like some of the digits are actually
# spelled out with letters: one, two, three, four, five, six, seven, eight, and nine
# also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last
# digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
# Adding these together produces 281.

# What is the sum of all of the calibration values?
from collections import namedtuple  # Similar to a struct. Note for Rust version

numberLookUp = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9
}

NumberPosition = namedtuple('NumberPosition', ['number', 'start', 'end'])

def find_all_substring_indices(string: str, substring: str) -> list:
    """Find all start and end indices of a substring in a string."""
    indices = []
    start = 0
    while start < len(string):
        start = string.find(substring, start)
        if start == -1:
            break
        end = start + len(substring) - 1
        indices.append((start, end))
        start = end + 1
    return indices

def find_edge_numbers(string: str) -> str:
    """Find the first and last number in a string."""
    numbers_found = []
    for key, value in numberLookUp.items():
        for start, end in find_all_substring_indices(string, key):
            numbers_found.append(NumberPosition(value, start, end))

    numbers_found.sort(key=lambda x: x.start)  # Sort by start index

    # If a calibration value has a number overlap e.g `eightwo` the first and last number together is 88
    first_number = numbers_found[0].number if numbers_found else 0
    last_number = numbers_found[-1].number if numbers_found[-1].start > numbers_found[0].end else numbers_found[0].number

    return f"{first_number}{last_number}"

if __name__ == "__main__":
    try:
        calibration_value_sum = 0
        with open('calibrations.txt') as file:
            for line in file:
                calibration_value_sum += int(find_edge_numbers(line.strip()))
        print(f"Total Calibrations: {calibration_value_sum}")
    except IOError as e:
        print(f"Error reading file: {e}")
