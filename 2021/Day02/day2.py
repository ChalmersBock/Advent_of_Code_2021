import os
import sys


def parse_input_question_1():

    horizontal_pos = 0
    depth = 0

    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        for line in file.readlines():
            action, amount_str = line.split(" ")
            amount = int(amount_str)

            if action == "forward":
                horizontal_pos += amount
            elif action == "down":
                depth += amount
            elif action == "up":
                depth -= amount
            else:
                print("Undefined action")

    print(f'Answer Q1: {horizontal_pos*depth}')


def parse_input_question_2():
    horizontal_pos = 0
    depth = 0
    aim = 0

    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        for line in file.readlines():
            action, amount_str = line.split(" ")
            amount = int(amount_str)

            if action == "forward":
                horizontal_pos += amount
                depth += (amount*aim)
            elif action == "down":
                aim += amount
            elif action == "up":
                aim -= amount
            else:
                print("Undefined action")

    print(f'Answer Q2: {horizontal_pos * depth}')


if __name__ == '__main__':
    parse_input_question_1()
    parse_input_question_2()


