import sys
import re
from collections import defaultdict


# We can ignore X, since X and Y don't affect each other with anything other than having to
# hit the box on the same iteration. However, X can stop in the box, giving Y infinitely many
# iterations to get to the box, which is what were looking for when wanting to reach high up
def calculate_max_y(positions):
    largest_y = -sys.maxsize
    for pos in positions:
        largest_y = max(largest_y, pos[1])

    highest_y = 0
    for i in range (largest_y, 0, -1):
        highest_y += i

    print(f'Highest possible y: {highest_y}')


def find_possible_x_angles(box, info_dict):
    infinity_list = []
    for x_start in range(box["x_upper"]+1):
        keep_simulating = True
        x_pos = 0
        iterations = 0
        while keep_simulating:
            x_pos += max(0, x_start-iterations)
            iterations += 1
            if box["x_upper"] >= x_pos >= box["x_lower"]:
                info_dict["x"][iterations].append(x_start)
                if x_start-iterations <= 0:
                    keep_simulating = False
                    infinity_list.append({"x_start": x_start, "smallest_iter": iterations})
            elif box["x_upper"] < x_pos or x_start-iterations <= 0:
                keep_simulating = False

    return infinity_list


def find_possible_y_angles(box, info_dict, infinity_list):

    for y_start in range(box["y_lower"], 1000):
        keep_simulating = True
        y_pos = 0
        iterations = 0
        while keep_simulating:
            y_pos += (y_start-iterations)
            iterations += 1
            if box["y_upper"] >= y_pos >= box["y_lower"]:
                info_dict["y"][iterations].append(y_start)
            elif box["y_lower"] > y_pos:
                keep_simulating = False

    for key in info_dict["y"]:
        for infinity_dict in infinity_list:
            if key > infinity_dict["smallest_iter"]:
                info_dict["x"][key].append(infinity_dict["x_start"])


def calculate_all_possible_angles(box):
    info_dict = {"x": defaultdict(list), "y": defaultdict(list)}

    infinity_list = find_possible_x_angles(box, info_dict)
    find_possible_y_angles(box, info_dict, infinity_list)

    positions = set()
    for iter_key in [elem for elem in info_dict["x"] if elem in info_dict["y"]]:
        for i in info_dict["x"][iter_key]:
            for j in info_dict["y"][iter_key]:
                positions.add((i, j))

    calculate_max_y(positions)
    print(f'Number of possible angles: {len(positions)}')


def main():
    with open("data", "r", encoding='utf-8') as file:
        line = file.readline().strip()
        x_1, x_2, y_1, y_2 = re.findall(r"[-]*[0-9]{1,3}", line)
        box = {
            "x_lower": min(int(x_1), int(x_2)),
            "x_upper": max(int(x_1), int(x_2)),
            "y_lower": min(int(y_1), int(y_2)),
            "y_upper": max(int(y_1), int(y_2)),
        }
    calculate_all_possible_angles(box)


if __name__ == '__main__':
    main()
