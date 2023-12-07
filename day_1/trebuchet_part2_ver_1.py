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
numberLookUp = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9
}

def find_all_substring_indices(string: str, substring: str) -> list:
    indices = []
    start = 0
    while start < len(string):
        start = string.find(substring, start)
        if start == -1:
            break
        end = start + len(substring) - 1
        indices.append((start, end))
        # Move start index to just after end
        start = end + 1
    return indices

def find_first_and_last_number_in_string(string: str) -> None:
    # Find all numbers in string
    numbers_found = {}
    startKey = 1
    for key in numberLookUp.keys():
        indices = find_all_substring_indices(string, key)
        if indices:
            for i in indices:
                numbers_found[str(startKey)] = [numberLookUp.get(key), i[0], i[1]]
                startKey += 1

    # Find the first and last numbers in string
    firstNumber = 0
    lastNumber = 0
    firstNumberStart = float('inf')
    lastNumberEnd = 0
    for key, value in numbers_found.items():
        if value[1] < firstNumberStart:
            firstNumber = value[0]
            firstNumberStart = value[1]
        if value[2] >= lastNumberEnd:
            lastNumber = value[0]
            lastNumberEnd = value[2]
    return f"{firstNumber}{lastNumber}"

if __name__ == "__main__":
    calibration_value_sum = 0
    with open('calibrations.txt') as file:
        for line in file:
            value = line.rstrip()
            calibration_value_sum += int(find_first_and_last_number_in_string(value))

    print(f"Total Calibrations: {calibration_value_sum}")
