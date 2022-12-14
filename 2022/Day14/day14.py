def find_max_min(rows, with_floor):
    x_min, x_max, y_max = 1000, 0, 0

    for row in rows:
        for coord in row:
            x_max = coord[0] if coord[0] > x_max else x_max
            x_min = coord[0] if coord[0] < x_min else x_min
            y_max = coord[1] if coord[1] > y_max else y_max

    x_length = x_max-x_min + 1
    y_length = y_max + 1
    adjustment_x = x_min

    if with_floor:
        y_length += 2
        if x_length < y_max*2:
            move = y_max - int(x_length/2)
            adjustment_x -= move
            x_length = y_max*2 + 1

    return x_length, y_length, adjustment_x


def place_stones(grid, rows, x_adjust):
    for row in rows:
        for i in range(len(row)-1):
            x_val, y_val, x_next, y_next = row[i][0], row[i][1], row[i+1][0], row[i+1][1]
            x_diff = x_next-x_val
            y_diff = y_next-y_val
            if x_diff > 0:
                for j in range(x_val, x_next+1):
                    grid[y_val][j-x_adjust] = "#"
            elif x_diff < 0:
                for j in range(x_val, x_next-1, -1):
                    grid[y_val][j-x_adjust] = "#"
            elif y_diff > 0:
                for j in range(y_val, y_next+1):
                    grid[j][x_val-x_adjust] = "#"
            elif y_diff < 0:
                for j in range(y_val, y_next-1, -1):
                    grid[j][x_val-x_adjust] = "#"
    return grid


def drop_sand(grid, start, with_floor):
    sand_inside = True
    sand_falling = False
    sand_pos = {
        "x": start,
        "y": 0
    }
    nbr_sand = 0

    while sand_inside:
        if not sand_falling:
            for line in grid:
                print(line)
            nbr_sand += 1
            sand_falling = True
            sand_pos = {
                "x": start,
                "y": 0
            }
        else:
            if sand_pos["y"] + 1 == len(grid) or sand_pos["x"] - 1 < 0 or sand_pos["x"] + 1 > len(grid[0]):
                print("here")
                print(sand_pos)
                return nbr_sand - 1
            else:
                if grid[sand_pos["y"]+1][sand_pos["x"]] == ".":
                    sand_pos["y"] += 1
                elif grid[sand_pos["y"]+1][sand_pos["x"]-1] == ".":
                    sand_pos["y"] += 1
                    sand_pos["x"] -= 1
                elif grid[sand_pos["y"]+1][sand_pos["x"]+1] == ".":
                    sand_pos["y"] += 1
                    sand_pos["x"] += 1
                else:
                    grid[sand_pos["y"]][sand_pos["x"]] = "o"
                    sand_falling = False
                    if with_floor and sand_pos["y"] == 0:
                        return nbr_sand


def parse_map(with_floor):
    rows = []

    with open("test", "r", encoding='utf-8') as file:
        for line in [line.strip() for line in file.readlines()]:
            row = []
            for coord in line.split(" -> "):
                x, y = coord.split(",")
                row.append((int(x), int(y)))
            rows.append(row)

    x_max, y_max, x_adjust = find_max_min(rows, with_floor)

    grid = []
    for i in range(y_max):
        grid_row = []
        for j in range(x_max + 1):
            grid_row.append(".")
        grid.append(grid_row)
    grid = place_stones(grid, rows, x_adjust)

    if with_floor:
        for i in range(len(grid[0])):
            grid[len(grid)-1][i] = "#"
    return grid, x_adjust


def calculate_units_of_sand(with_floor):
    grid, x_adjust = parse_map(with_floor)

    units_of_sand = drop_sand(grid, 500-x_adjust, with_floor)

    print("The number of units of sand before one fall out is: ", units_of_sand)


if __name__ == '__main__':
    #calculate_units_of_sand(False)
    calculate_units_of_sand(True)
