def parse_grid():
    grid = []
    with open("data", "r", encoding='utf-8') as file:
        for line in [line.strip() for line in file.readlines()]:
            row = []
            for height in line:
                row.append(int(height))
            grid.append(row)
    return grid


def count_visible_trees():
    grid = parse_grid()
    visible_trees = 0

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            blocked = 0
            for a in range(j-1, -1, -1):  # Check left
                if grid[i][a] >= grid[i][j]:
                    blocked += 1
                    break
            for a in range(j + 1, len(grid[i])):  # Check right
                if grid[i][a] >= grid[i][j]:
                    blocked += 1
                    break
            for a in range(i - 1, -1, -1):  # Check up
                if grid[a][j] >= grid[i][j]:
                    blocked += 1
                    break
            for a in range(i + 1, len(grid)):  # Check down
                if grid[a][j] >= grid[i][j]:
                    blocked += 1
                    break
            if blocked != 4:
                visible_trees += 1

    always_visible = len(grid) * len(grid[0]) - (len(grid) - 2) * (len(grid[0]) - 2)
    visible_trees += always_visible

    return visible_trees


def count_view_score():
    grid = parse_grid()
    high_score = 0

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            score = 1
            counter = 0
            for a in range(j-1, -1, -1):  # Check left
                if grid[i][a] < grid[i][j]:
                    counter += 1
                elif grid[i][a] >= grid[i][j]:
                    counter += 1
                    break
            score *= counter
            counter = 0

            for a in range(j + 1, len(grid[i])):  # Check right
                if grid[i][a] < grid[i][j]:
                    counter += 1
                elif grid[i][a] >= grid[i][j]:
                    counter += 1
                    break
            score *= counter
            counter = 0

            for a in range(i - 1, -1, -1):  # Check up
                if grid[a][j] < grid[i][j]:
                    counter += 1
                elif grid[a][j] >= grid[i][j]:
                    counter += 1
                    break
            score *= counter
            counter = 0

            for a in range(i + 1, len(grid)):  # Check down
                if grid[a][j] < grid[i][j]:
                    counter += 1
                elif grid[a][j] >= grid[i][j]:
                    counter += 1
                    break
            score *= counter

            if score > high_score:
                high_score = score

    return high_score


if __name__ == '__main__':
    print("Number of visible trees are: " + str(count_visible_trees()))
    print("Tree with highest score has: " + str(count_view_score()))
