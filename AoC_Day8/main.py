import os
import sys
import re


def remove_chars(chars, string):
    new_string = string
    for char in chars:
        new_string = re.sub(char, "", new_string)

    return new_string


# Only necessary to figure out the positions TopRight, Middle, and BottomLeft to be able to tell all numbers apart
class Decoder:

    def __init__(self, inp):
        self.text_codes = ['' for _ in range(10)]
        self.display = {}

        codes = []
        numbers_code = inp.strip().split(" ")
        for code in numbers_code:
            codes.append(code)

        for code in codes:
            if len(code) == 2:
                self.text_codes[1] = code
            elif len(code) == 4:
                self.text_codes[4] = code
            elif len(code) == 7:
                self.text_codes[8] = code

            if self.text_codes[1] and self.text_codes[4] and self.text_codes[8]:
                break

        middle_and_top_left = list(remove_chars(self.text_codes[1], self.text_codes[4]))
        for code in codes:
            if len(code) == 6:
                if middle_and_top_left[0] not in code or middle_and_top_left[1] not in code:
                    self.text_codes[0] = code
                    break

        if middle_and_top_left[0] in self.text_codes[0]:
            self.display["Middle"] = middle_and_top_left[1]
        else:
            self.display["Middle"] = middle_and_top_left[0]

        for code in codes:
            if len(code) == 5:
                if len(remove_chars(code, self.text_codes[4])) == 1 \
                        and len(remove_chars(code, self.text_codes[1])) != 0:
                    self.text_codes[5] = code
                    break

        self.display["TopRight"] = remove_chars(self.text_codes[5], self.text_codes[1])

        self.display["BottomLeft"] = remove_chars(
            self.display["TopRight"],
            remove_chars(self.text_codes[5], self.text_codes[8])
        )

    def get_dict(self):
        return self.display


class DisplayNumber:

    def __init__(self, dec, code):
        self.number_value = -1

        if len(code) == 2:
            self.number_value = 1
        elif len(code) == 3:
            self.number_value = 7
        elif len(code) == 4:
            self.number_value = 4
        elif len(code) == 7:
            self.number_value = 8
        elif len(code) == 5:
            if dec.get_dict()["BottomLeft"] in code:
                self.number_value = 2
            elif dec.get_dict()["TopRight"] in code:
                self.number_value = 3
            else:
                self.number_value = 5
        else:
            if dec.get_dict()["Middle"] in code:
                if dec.get_dict()["TopRight"] in code:
                    self.number_value = 9
                else:
                    self.number_value = 6
            else:
                self.number_value = 0

    def get_number_value(self):
        return self.number_value


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
            dec = Decoder(inp)

            numbers = ""
            for code in numbers_code:
                numbers += str(DisplayNumber(dec, code).get_number_value())
            output_sum += int(numbers)

    print(f'Output Sum: {output_sum}')


if __name__ == '__main__':
    count_unique_digits_in_output()
    sum_of_outputs()

