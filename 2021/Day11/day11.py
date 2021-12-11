def parse_file():
    octopus_grid = []
    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            row = []
            for digit in line:
                row.append({"value": int(digit), "flash": False})
            octopus_grid.append(row)

    return octopus_grid


def increment_grid(octopus_grid):
    for i, row in enumerate(octopus_grid):
        for j, _ in enumerate(row):
            octopus_grid[i][j]["value"] += 1


def calculate_chain_reaction(octopus_grid):
    change = True
    new_flashes = 0
    while change:
        change = False
        for i, row in enumerate(octopus_grid):
            for j, octo in enumerate(row):
                if not octo["flash"] and octo["value"] > 9:
                    change = True
                    octo["flash"] = True
                    increment_neighbours(octopus_grid, i, j)
                    new_flashes += 1
    return new_flashes


def increment_neighbours(octopus_grid, y_pos, x_pos):
    if x_pos > 0:
        octopus_grid[y_pos][x_pos - 1]["value"] += 1
        if y_pos > 0:
            octopus_grid[y_pos - 1][x_pos - 1]["value"] += 1
    if y_pos > 0:
        octopus_grid[y_pos - 1][x_pos]["value"] += 1
        if x_pos < len(octopus_grid[y_pos]) - 1:
            octopus_grid[y_pos - 1][x_pos + 1]["value"] += 1

    if x_pos < len(octopus_grid[y_pos]) - 1:
        octopus_grid[y_pos][x_pos + 1]["value"] += 1
        if y_pos < len(octopus_grid)-1:
            octopus_grid[y_pos + 1][x_pos + 1]["value"] += 1
    if y_pos < len(octopus_grid) - 1:
        octopus_grid[y_pos + 1][x_pos]["value"] += 1
        if x_pos > 0:
            octopus_grid[y_pos + 1][x_pos - 1]["value"] += 1


def turn_off_flashes(octopus_grid):
    for i, row in enumerate(octopus_grid):
        for j, _ in enumerate(row):
            if octopus_grid[i][j]["flash"]:
                octopus_grid[i][j]["flash"] = False
                octopus_grid[i][j]["value"] = 0


def calculate_total_flashes(steps):
    octopus_grid = parse_file()
    total_flashes = 0
    for _ in range(steps):
        increment_grid(octopus_grid)
        total_flashes += calculate_chain_reaction(octopus_grid)
        turn_off_flashes(octopus_grid)

    print(f'Number of flashes in {steps} steps: {total_flashes}')


def calculate_first_full_synchronization():
    octopus_grid = parse_file()
    no_sync = True
    size = sum(len(row) for row in octopus_grid)
    steps = 0
    while no_sync:
        steps += 1
        increment_grid(octopus_grid)
        flashes = calculate_chain_reaction(octopus_grid)
        turn_off_flashes(octopus_grid)

        if flashes == size:
            no_sync = False

    print(f'Number of steps before full sync: {steps}')


if __name__ == '__main__':
    calculate_total_flashes(100)
    calculate_first_full_synchronization()