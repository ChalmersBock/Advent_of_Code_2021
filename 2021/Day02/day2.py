import os
import sys


def find_position(with_aim):
    horizontal_pos = 0
    depth = 0
    down_up_value = 0

    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        for line in file.readlines():
            action, amount_str = line.split(" ")
            amount = int(amount_str)

            if action == "forward":
                horizontal_pos += amount
                if with_aim:
                    depth += (amount*down_up_value)
            elif action == "down":
                down_up_value += amount
            elif action == "up":
                down_up_value -= amount
            else:
                print(f'Undefined action: {action}')

            if not with_aim:
                depth = down_up_value

    print(f'Answer Q2: {horizontal_pos * depth}')


if __name__ == '__main__':
    find_position(False)
    find_position(True)


