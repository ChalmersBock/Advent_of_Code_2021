import math
import copy
import regex


class Value:
    def __init__(self, value):
        self.value = value
        self.depth = 0

    def update_depth(self, depth):
        self.depth = depth - 1

    def get_depth(self):
        return self.depth

    def add_right(self, value):
        self.value += value

    def add_left(self, value):
        self.value += value

    def calculate_magnitude(self):
        return self.value

    def to_string(self):
        return str(self.value)


class Pair:

    def __init__(self, left, right):
        self.right = right
        self.left = left
        self.depth = 0

    def update_depth(self, depth):
        self.depth = depth
        self.right.update_depth(depth + 1)
        self.left.update_depth(depth + 1)

    def get_depth(self):
        return max(self.left.get_depth(), self.right.get_depth())

    def add_right(self, value):
        self.right.add_right(value)

    def add_left(self, value):
        self.left.add_left(value)

    def explode(self):
        if self.left.get_depth() == self.depth and self.right.get_depth() == self.depth:
            return self.left, self.right, True

        if self.left.get_depth() >= 4:
            new_left, new_right, exploded = self.left.explode()
            if exploded:
                self.left = Value(0)
                self.right.add_left(new_right.value)
                return new_left, None, False
            if new_right is not None:
                self.right.add_left(new_right.value)
                return None, None, False
        elif self.right.get_depth() >= 4:
            new_left, new_right, exploded = self.right.explode()
            if exploded:
                self.right = Value(0)
                self.left.add_right(new_left.value)
                return None, new_right, False
            if new_left is not None:
                self.left.add_right(new_left.value)
                return None, None, False

        return new_left, new_right, exploded

    def attempt_split(self):
        if self.left.get_depth() == self.depth:
            if self.left.value > 9:
                value = self.left.value
                self.left = Pair(Value(math.floor(value/2)), Value(math.ceil(value/2)))
                return True
            if self.right.get_depth() == self.depth:
                if self.right.value > 9:
                    value = self.right.value
                    self.right = Pair(Value(math.floor(value/2)), Value(math.ceil(value/2)))
                    return True
            elif self.right.attempt_split():
                return True
        elif self.left.attempt_split():
            return True
        elif self.right.get_depth() != self.depth:
            if self.right.attempt_split():
                return True
        elif self.right.get_depth() == self.depth and self.right.value > 9:
            value = self.right.value
            self.right = Pair(Value(math.floor(value / 2)), Value(math.ceil(value / 2)))
            return True

        return False

    def calculate_magnitude(self):
        return 3*self.left.calculate_magnitude() + 2*self.right.calculate_magnitude()

    def to_string(self):
        return f'[{self.left.to_string()}, {self.right.to_string()}]'


def parse_file():
    with open("data", "r", encoding='utf-8') as file:
        numbers = []
        for line in [x.strip() for x in file.readlines()]:
            pair = parse_pair(line)
            numbers.append(pair)

    return numbers


def value_or_pair(match):
    if len(match) == 1:
        return Value(int(match))
    return parse_pair(match)


def parse_pair(pair):
    full_match = regex.match(r"^(\[((?1)),((?1))\]|\d)$", pair)
    left_match = full_match.group(2)
    right_match = full_match.group(3)

    return Pair(value_or_pair(left_match), value_or_pair(right_match))


def calculate_magnitude_of_file(numbers):
    current_pair = numbers[0]
    for i in range(1, len(numbers)):
        current_pair = Pair(current_pair, numbers[i])
        reduced = True
        while reduced:
            reduced = False
            current_pair.update_depth(0)
            if current_pair.get_depth() >= 4:
                current_pair.explode()
                reduced = True
            elif current_pair.attempt_split():
                reduced = True

    magnitude = current_pair.calculate_magnitude()

    return magnitude


def find_biggest_combo(numbers):
    largest_magnitude = 0
    for i, number_one in enumerate(numbers):
        for j, number_two in enumerate(numbers):
            if i != j:
                magnitude = calculate_magnitude_of_file(copy.deepcopy([number_one, number_two]))
                largest_magnitude = max(magnitude, largest_magnitude)

    print(f'The largest magnitude of two numbers is: {largest_magnitude}')


def main():
    parsed_numbers = parse_file()
    file_magnitude = calculate_magnitude_of_file(copy.deepcopy(parsed_numbers))
    print(f'The magnitude is: {file_magnitude}')
    parsed_numbers = parse_file()
    find_biggest_combo(parsed_numbers)


if __name__ == '__main__':
    main()

