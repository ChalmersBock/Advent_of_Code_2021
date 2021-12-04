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
    queue = []

    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        for line in file.readlines():
            new_value = int(line)
            if len(queue) < 3:
                queue.append(new_value)
            else:
                old_depth = sum(queue)
                queue.append(new_value)
                queue.pop(0)
                new_depth = sum(queue)
                if new_depth > old_depth:
                    counter += 1

    return counter


if __name__ == '__main__':
    increases = count_increase()
    print(increases)

    increases_block = count_block_increase()
    print(increases_block)
