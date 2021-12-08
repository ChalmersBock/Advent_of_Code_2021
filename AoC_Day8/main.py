import os
import sys
import re


def remove_chars(chars, string):
    for char in chars:
        string = re.sub(char, "", string)

    return string


# The idea is: Get 1/4 from length -> 0 -> Middle -> 5 -> TopRight -> BottomLeft
# All other positions and numbers are not necessary to get enough info to tell them apart
def decode_input(inp):
    text_codes = ['' for _ in range(10)]
    display = {}

    codes = []
    numbers_code = inp.strip().split(" ")
    for code in numbers_code:
        codes.append(code)

    for code in codes:
        if len(code) == 2:
            text_codes[1] = code
        elif len(code) == 4:
            text_codes[4] = code

    first_char, second_char = list(remove_chars(text_codes[1], text_codes[4]))
    for code in codes:
        if len(code) == 6 and (first_char not in code or second_char not in code):
            text_codes[0] = code
            break

    display["Middle"] = first_char
    if first_char in text_codes[0]:
        display["Middle"] = second_char

    for code in codes:
        if (len(code) == 5
                and len(remove_chars(code, text_codes[4])) == 1
                and len(remove_chars(code, text_codes[1])) != 0):
            text_codes[5] = code
            break

    display["TopRight"] = remove_chars(text_codes[5], text_codes[4])
    display["BottomLeft"] = remove_chars(
        display["TopRight"],
        remove_chars(text_codes[5], text_codes[0])
    )
    return display


def get_number_from_code(dec, code):

    if len(code) == 2:
        number_value = 1
    elif len(code) == 3:
        number_value = 7
    elif len(code) == 4:
        number_value = 4
    elif len(code) == 7:
        number_value = 8
    elif len(code) == 5:
        if dec["BottomLeft"] in code:
            number_value = 2
        elif dec["TopRight"] in code:
            number_value = 3
        else:
            number_value = 5
    else:
        if dec["Middle"] in code:
            if dec["TopRight"] in code:
                number_value = 9
            else:
                number_value = 6
        else:
            number_value = 0

    return number_value


def count_unique_digits_in_output():
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        counter = 0
        for line in file.readlines():
            _, output = line.split("|")
            numbers = output.strip().split(" ")

            for nbr in numbers:
                if len(nbr) in [2, 3, 4, 7]:  # Size of 1, 7, 4, 8 being displayed
                    counter += 1
    print(f'Unique digits in output: {counter}')


def sum_of_outputs():
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        output_sum = 0
        for line in file.readlines():
            inp, output = line.split("|")
            numbers_code = output.strip().split(" ")

            numbers = ""
            dec = decode_input(inp)
            for code in numbers_code:
                numbers += str(get_number_from_code(dec, code))
            output_sum += int(numbers)

    print(f'Output Sum: {output_sum}')


if __name__ == '__main__':
    count_unique_digits_in_output()
    sum_of_outputs()

