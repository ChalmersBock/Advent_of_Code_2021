import os
import sys


def lava_tubes(height_map):
    total_sum = 0
    lowest_points = []

    for i, row in enumerate(height_map):
        for j, value in enumerate(row):
            if (not (j > 0 and height_map[i][j] >= height_map[i][j-1])
                    and not (i > 0 and height_map[i][j] >= height_map[i-1][j])
                    and not (j < len(height_map[i])-1 and height_map[i][j] >= height_map[i][j+1])
                    and not (i < len(height_map)-1 and height_map[i][j] >= height_map[i+1][j])):
                total_sum += value + 1
                lowest_points.append({"x": j, "y": i})

    print(f'Sum of risk level: {total_sum}')
    return lowest_points


def largest_basins(height_map, points):
    basin_sizes = []

    for start_point in points:
        stack = [start_point]
        visited_points = []
        basin_size = 0

        while len(stack) != 0:
            current_point = stack.pop()
            j = current_point['x']
            i = current_point['y']
            if height_map[i][j] == 9 or current_point in visited_points:
                continue
            visited_points.append(current_point)
            basin_size += 1

            if j > 0 and height_map[i][j] < height_map[i][j-1]:
                stack.append({"x": j-1, "y": i})
            if i > 0 and height_map[i][j] < height_map[i-1][j]:
                stack.append({"x": j, "y": i-1})
            if j < len(height_map[i])-1 and height_map[i][j] < height_map[i][j+1]:
                stack.append({"x": j+1, "y": i})
            if i < len(height_map)-1 and height_map[i][j] < height_map[i+1][j]:
                stack.append({"x": j, "y": i+1})
        basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    top_3 = basin_sizes[:3]

    print(f'Basin sizes: {top_3[0]*top_3[1]*top_3[2]}')


def parse_file():
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        height_map = []
        for line in file.readlines():
            row = []
            line = line.strip()
            for digit in line:
                row.append(int(digit))
            height_map.append(row)
    return height_map


if __name__ == '__main__':
    lava_map = parse_file()
    low_points = lava_tubes(lava_map)
    largest_basins(lava_map, low_points)
