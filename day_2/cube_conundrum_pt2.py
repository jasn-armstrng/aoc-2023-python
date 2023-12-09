def parse_game_results(cubes: dict, game: str) -> tuple:
    game_id = ""
    sets = {key: [] for key in cubes.keys()}
    current_number = ''
    current_string = ''

    for char in game:
        if char.isdigit():
            current_number += char
        elif char.isalpha():
            current_string += char
        else:
            if char == ':' and current_number:
                game_id += current_number

            if current_number and current_string:
                if current_string in sets:
                    sets[current_string].append(int(current_number))
                current_string = ''
                current_number = ''

    if current_number and current_string:
        if current_string in sets:
            sets[current_string].append(int(current_number))

    return (int(game_id), sets)  # e.g. (1, {'red': [7, 4, 3], 'green': [5, 16, 11], 'blue': [4, 3]})


def calc_game_power(game_results: tuple) -> int:
    power = 1
    for _, value in game_results[1].items():
        power *= max(value)
    return power


if __name__ == "__main__":
    sum_of_powers = 0
    cubes = { "red": 12, "green": 13, "blue": 14 }
    with open("puzzle.txt") as file:
        for line in file:
            game = line.strip()
            game_results = parse_game_results(cubes, game)
            sum_of_powers += calc_game_power(game_results)
    print(f"Sum: {sum_of_powers}")
