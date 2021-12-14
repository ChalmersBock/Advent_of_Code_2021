from collections import Counter


def parse_file():
    with open("data", "r", encoding='utf-8') as file:
        code_line = file.readline().strip()
        file.readline()  # Empty line

        symbol_dict = {}
        symbol_occurrences = {}
        char_occurrences = {}
        for key, value in [x.strip().split("->") for x in file.readlines()]:
            symbol_dict[key.strip()] = value.strip()
            symbol_occurrences[key.strip()] = 0
            char_occurrences[value.strip()] = 0

        for i, value in enumerate(code_line):
            char_occurrences[value] += 1
            if i != len(code_line)-1:
                symbol_occurrences[value + code_line[i+1]] += 1

    return symbol_occurrences, symbol_dict, char_occurrences


def simulate_polymerization(symbol_occurrences, symbol_dict, char_occurrences, steps):
    current_occurrences = symbol_occurrences

    for _ in range(steps):
        new_occurrences = {}
        for key in current_occurrences:
            new_occurrences[key] = 0

        for key in current_occurrences:
            new_occurrences[(key[0] + symbol_dict[key])] += current_occurrences[key]
            new_occurrences[(symbol_dict[key] + key[1])] += current_occurrences[key]
            char_occurrences[symbol_dict[key]] += current_occurrences[key]

        current_occurrences = new_occurrences

    counts = Counter(char_occurrences)
    largest = counts.most_common()[0][1]
    smallest = counts.most_common()[-1][1]

    print(f'({steps} steps) Most common element minus least common element: {largest-smallest}')


def main():
    symbol_occurrences, char_dict, char_occurrences = parse_file()
    simulate_polymerization(symbol_occurrences, char_dict, char_occurrences, 10)
    symbol_occurrences, char_dict, char_occurrences = parse_file()
    simulate_polymerization(symbol_occurrences, char_dict, char_occurrences, 40)


if __name__ == '__main__':
    main()
