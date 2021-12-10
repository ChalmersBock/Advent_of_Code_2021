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


def find_rating(nbr_list, iteration, oxygen):
    if len(nbr_list) == 0 or len(nbr_list[0]) < iteration:
        print("Something went wrong")
        return -1

    counter = 0
    for nbr in nbr_list:
        if nbr[iteration] == "1":
            counter += 1
        else:
            counter -= 1

    new_list = []
    key = "0"
    if counter < 0:
        if not oxygen:
            key = "1"
    elif oxygen:
        key = "1"

    for nbr in nbr_list:
        if nbr[iteration] == key:
            new_list.append(nbr)

    if len(new_list) == 1:
        return new_list[0]
    else:
        return find_rating(new_list, iteration+1, oxygen)


def parse_input_question_2():
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        number_list = [x.strip("\n") for x in file.readlines()]

        oxygen_rating_str = find_rating(number_list, 0, True)
        co2_rating_str = find_rating(number_list, 0, False)

    oxygen_rating = int(oxygen_rating_str, 2)
    co2_rating = int(co2_rating_str, 2)

    print(f'Answer Q2: {oxygen_rating*co2_rating}')


if __name__ == '__main__':
    parse_input_question_1()
    parse_input_question_2()

