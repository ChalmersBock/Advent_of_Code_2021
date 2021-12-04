import os
import sys


def count_increase():

    counter = 0
    current_depth = -1

    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        for line in file.readlines():
            depth = int(line)
            if current_depth != -1 and depth > current_depth:
                counter += 1
            current_depth = depth

    return counter


def count_block_increase():

    counter = 0
    current_block_depth = -1

    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        for line in file.readlines():
            depth = int(line)
            if current_depth != -1 and depth > current_depth:
                counter += 1
            current_depth = depth

    return counter

if __name__ == '__main__':
    increases = count_increase()
    print(increases)

    increases2 = count_block_increase()

