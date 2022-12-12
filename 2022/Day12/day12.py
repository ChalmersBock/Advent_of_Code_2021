import math

from dijkstar import Graph, find_path, algorithm


def pos_to_string(y, x):
    return str(y) + "_" + str(x)


def add_edges(graph, grid, y, x):
    current = grid[y][x] + 1
    if x > 0:
        if grid[y][x-1] <= current:
            graph.add_edge(pos_to_string(y, x), pos_to_string(y, x-1), 1)
    if x < len(grid[0])-1:
        if grid[y][x+1] <= current:
            graph.add_edge(pos_to_string(y, x), pos_to_string(y, x+1), 1)
    if y > 0:
        if grid[y-1][x] <= current:
            graph.add_edge(pos_to_string(y, x), pos_to_string(y-1, x), 1)
    if y < len(grid)-1:
        if grid[y+1][x] <= current:
            graph.add_edge(pos_to_string(y, x), pos_to_string(y+1, x), 1)

    return graph


def parse_map(start_pos):
    grid = []
    start_nodes = []
    end_node = ""

    with open("data", "r", encoding='utf-8') as file:
        y_counter = 0
        for line in [line.strip() for line in file.readlines()]:
            row = []
            x_counter = 0
            for char in line:
                if char in start_pos:
                    row.append(ord("a"))
                    start_nodes.append(pos_to_string(y_counter, x_counter))
                elif char == "E":
                    row.append(ord("z"))
                    end_node = pos_to_string(y_counter, x_counter)
                else:
                    row.append(ord(char))
                x_counter += 1
            grid.append(row)
            y_counter += 1

    graph = Graph()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            graph = add_edges(graph, grid, i, j)

    least_steps = math.inf
    for start in start_nodes:
        try:
            steps = len(find_path(graph, start, end_node).nodes)-1
            if steps < least_steps:
                least_steps = steps
        except algorithm.NoPathError:  # Ignore any points that do not have a path to the summit
            continue
    print("The fewest steps possible are: ", least_steps)


if __name__ == '__main__':
    parse_map(["S"])
    parse_map(["S", "a"])

