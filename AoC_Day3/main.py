import os
import sys


def parse_input_question_1():

    occurrence_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        for line in file.readlines():

            for index in range(12):
                if line[index] == "1":
                    occurrence_list[index] += 1
                else:
                    occurrence_list[index] -= 1

    gamma_str = ""
    epsilon_string = ""
    for elem in occurrence_list:
        if elem > 0:
            gamma_str += "1"
            epsilon_string += "0"
        else:
            gamma_str += "0"
            epsilon_string += "1"

    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_string, 2)

    print(f'Answer Q1: {gamma*epsilon}')


if __name__ == '__main__':
    parse_input_question_1()


