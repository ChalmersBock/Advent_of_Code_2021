from dijkstar import Graph, find_path


def add_edges(graph, grid, i, j):
    if j > 0:
        graph.add_edge(f'{i}_{j}', f'{i}_{j-1}', grid[i][j-1])
    if i > 0:
        graph.add_edge(f'{i}_{j}', f'{i-1}_{j}', grid[i-1][j])
    if j < len(grid[i]) - 1:
        graph.add_edge(f'{i}_{j}', f'{i}_{j+1}', grid[i][j+1])
    if i < len(grid) - 1:
        graph.add_edge(f'{i}_{j}', f'{i+1}_{j}', grid[i+1][j])


def parse_file(repetitions):
    grid = []
    for rep_y in range(repetitions):
        with open("data", "r", encoding='utf-8') as file:
            for line in [x.strip() for x in file.readlines()]:
                row = []
                for rep_x in range(repetitions):
                    for value in [int(x) for x in line]:
                        real_value = ((value + rep_y + rep_x - 1) % 9) + 1
                        if real_value > 9:
                            real_value = 1
                        row.append(real_value)
                grid.append(row)

    graph = Graph()
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            add_edges(graph, grid, i, j)
    start = "0_0"
    end = f'{len(grid)-1}_{len(grid[-1])-1}'

    return graph, start, end


def main():
    graph, start, end = parse_file(1)
    print(f'Shortest path length: {find_path(graph, start, end).total_cost}')
    graph, start, end = parse_file(5)
    print(f'Shortest path length: {find_path(graph, start, end).total_cost}')


if __name__ == '__main__':
    main()
