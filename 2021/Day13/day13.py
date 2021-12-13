def parse_file():
    with open("data", "r", encoding='utf-8') as file:
        positions = []
        folds = []
        for line in [x.rstrip() for x in file.readlines()]:
            if "," in line:
                x_pos, y_pos = line.split(",")
                pos = {"x": int(x_pos), "y": int(y_pos)}
                positions.append(pos)
            elif "fold" in line:
                _, _, axis_and_value = line.split(" ")
                axis, value = axis_and_value.split("=")
                folds.append({"axis": axis, "value": int(value)})

    largest_x = 2000  # Arbitrary
    for fold in folds:
        if fold["axis"] == "x":
            largest_x = (fold["value"]*2) + 1
            break
    largest_y = 2000  # Arbitrary
    for fold in folds:
        if fold["axis"] == "y":
            largest_y = (fold["value"]*2) + 1
            break

    start_grid = [[False] * largest_x for _ in range(largest_y)]

    for pos in positions:
        start_grid[pos["y"]][pos["x"]] = True

    return start_grid, folds


def fold_and_count_dots(base_grid, folds):
    if not folds:
        return base_grid

    fold = folds.pop(0)
    if fold["axis"] == "x":
        folded_grid = [[False] * (fold["value"]) for _ in range(len(base_grid))]
        for i in range(fold["value"]):
            for j, _ in enumerate(base_grid):
                folded_grid[j][i] = base_grid[j][i] or base_grid[j][len(base_grid[j]) - 1 - i]
    if fold["axis"] == "y":
        folded_grid = [[False] * len(base_grid[0]) for _ in range(fold["value"])]
        for j in range(fold["value"]):
            for i, _ in enumerate(base_grid[j]):
                folded_grid[j][i] = base_grid[j][i] or base_grid[len(base_grid) - 1 - j][i]

    return fold_and_count_dots(folded_grid, folds)


def visible_dots(base_grid, folds):
    new_grid = fold_and_count_dots(base_grid, folds)
    counter = 0
    for _, row in enumerate(new_grid):
        for _, value in enumerate(row):
            if value:
                counter += 1

    print(f'Visible dots: {counter}')


def secret_code(base_grid, folds):
    print("The secret code is:")
    for row in fold_and_count_dots(base_grid, folds):
        line = ""
        for elem in row:
            if elem:
                line += "O"
            else:
                line += " "
        print(line)


if __name__ == '__main__':
    grid, all_folds = parse_file()
    visible_dots(grid, [all_folds[0]])
    secret_code(grid, all_folds)
