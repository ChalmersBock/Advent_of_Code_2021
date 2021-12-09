import os
import sys


def lava_tubes(height_map):

    total_sum = 0
    lowest_points = []

    for y_coord in range(len(height_map)):
        for x_coord in range(len(height_map[y_coord])):
            counter = 0
            if x_coord > 0:
                if height_map[y_coord][x_coord] < height_map[y_coord][x_coord-1]:
                    counter += 1
            else:
                counter += 1

            if y_coord > 0:
                if height_map[y_coord][x_coord] < height_map[y_coord-1][x_coord]:
                    counter += 1
            else:
                counter += 1

            if x_coord < len(height_map[y_coord])-1:
                if height_map[y_coord][x_coord] < height_map[y_coord][x_coord+1]:
                    counter += 1
            else:
                counter += 1
            if y_coord < len(height_map)-1:
                if height_map[y_coord][x_coord] < height_map[y_coord+1][x_coord]:
                    counter += 1
            else:
                counter += 1

            if counter == 4:
                total_sum += height_map[y_coord][x_coord] + 1
                lowest_points.append({"x": x_coord, "y": y_coord})

    print(f'Sum of risk level: {total_sum}')
    return lowest_points


def largest_basins(height_map, points):

    basin_sizes = []

    for start_point in points:
        stack = [start_point]
        visited_points = [start_point]
        basin_size = 0

        while len(stack) != 0:
            current_point = stack.pop()
            x = current_point['x']
            y = current_point['y']
            if height_map[y][x] == 9:
                continue
            basin_size += 1

            if x > 0:
                if height_map[y][x] < height_map[y][x-1]:
                    point = {"x": x-1, "y": y}
                    if point not in visited_points:
                        stack.append(point)
                        visited_points.append(point)
            if y > 0:
                if height_map[y][x] < height_map[y-1][x]:
                    point = {"x": x, "y": y-1}
                    if point not in visited_points:
                        stack.append(point)
                        visited_points.append(point)
            if x < len(height_map[y])-1:
                if height_map[y][x] < height_map[y][x+1]:
                    point = {"x": x+1, "y": y}
                    if point not in visited_points:
                        stack.append(point)
                        visited_points.append(point)
            if y < len(height_map)-1:
                if height_map[y][x] < height_map[y+1][x]:
                    point = {"x": x, "y": y+1}
                    if point not in visited_points:
                        stack.append(point)
                        visited_points.append(point)
        basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    top_3 = basin_sizes[:3]

    print(f'Basin sizes: {top_3[0]*top_3[1]*top_3[2]}')


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        lava_map = []
        for line in file.readlines():
            row = []
            line = line.strip()
            for digit in line:
                row.append(int(digit))
            lava_map.append(row)

    low_points = lava_tubes(lava_map)
    largest_basins(lava_map, low_points)

