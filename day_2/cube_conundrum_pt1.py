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

    return (int(game_id), sets)


def is_valid_game(cubes: dict, game_results: tuple) -> int:
    for key, value in cubes.items():
        if max(game_results[1].get(key)) > value:
            return 0
    return game_results[0] if game_results[0] is not None else 0


if __name__ == "__main__":
    sum = 0
    cubes = { "red": 12, "green": 13, "blue": 14 }

    with open("puzzle.txt") as file:
        for line in file:
            game = line.strip()
            game_results = parse_game_results(cubes, game)
            valid_game_id = is_valid_game(cubes, game_results)
            sum += valid_game_id

    print(f"Sum: {sum}")
