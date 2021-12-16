import sys

hex_to_bit_dict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}



class Package:

    def __init__(self):
        self.version = -1
        self.type_id = -1
        self.value = -1
        self.length_id = -1
        self.sub_packages = []

    def calculate_package(self):
        value = 0
        if self.type_id == 0:
            value = 0
            for package in self.sub_packages:
                value += package.calculate_package()
        elif self.type_id == 1:
            value = 1
            for package in self.sub_packages:
                value *= package.calculate_package()
        elif self.type_id == 2:
            value = sys.maxsize
            for package in self.sub_packages:
                value = min(value, package.calculate_package())
        elif self.type_id == 3:
            value = -1
            for package in self.sub_packages:
                value = max(value, package.calculate_package())
        elif self.type_id == 4:
            value = self.value
        elif self.type_id == 5:
            value = 0
            if self.sub_packages[0].calculate_package() > self.sub_packages[1].calculate_package():
                value = 1
        elif self.type_id == 6:
            value = 0
            if self.sub_packages[0].calculate_package() < self.sub_packages[1].calculate_package():
                value = 1
        elif self.type_id == 7:
            value = 0
            if self.sub_packages[0].calculate_package() == self.sub_packages[1].calculate_package():
                value = 1
        return value


def parse_bits(bit_stack, number_of_bits):
    bits = ""
    for _ in range(number_of_bits):
        bits += bit_stack.pop()
    return bits


def parse_bits_to_int(bit_stack, number_of_bits):
    return int(parse_bits(bit_stack, number_of_bits), 2)


def parse_literal_value(bit_stack, can_have_trail):
    last_bits = False
    full_bit_string = ""
    while not last_bits:
        bit_string = parse_bits(bit_stack, 5)
        if bit_string[0] == '0':
            last_bits = True
        full_bit_string += bit_string[1:]
        if can_have_trail and '1' not in bit_stack:
            break  # Trailing 0s
    return int(full_bit_string, 2)


def identify_package(bit_stack, can_have_trail):
    package = Package()

    package.version = parse_bits_to_int(bit_stack, 3)
    package.type_id = parse_bits_to_int(bit_stack, 3)

    if package.type_id != 4:
        package.length_id = parse_bits_to_int(bit_stack, 1)

        if package.length_id == 0:
            length_of_sub_packages = parse_bits_to_int(bit_stack, 15)
            small_stack = bit_stack[-length_of_sub_packages:]
            for _ in range(length_of_sub_packages):
                bit_stack.pop()

            while small_stack:
                package.sub_packages.append(identify_package(small_stack, False))

        elif package.length_id == 1:
            number_of_sub_packages = parse_bits_to_int(bit_stack, 11)
            for _ in range(number_of_sub_packages):
                package.sub_packages.append(identify_package(bit_stack, True))

    else:
        package.value = parse_literal_value(bit_stack, can_have_trail)

    return package


def parse_file():
    with open("data", "r", encoding='utf-8') as file:
        bit_string = ""
        for hex_char in file.readline().strip():
            bit_string += hex_to_bit_dict[hex_char]

    package = None
    bit_stack = []
    for bit in reversed(bit_string):
        bit_stack.append(bit)

    while bit_stack:
        package = identify_package(bit_stack, True)
        if '1' not in bit_stack:
            break  # Trailing 0s

    total_version_sum = 0
    package_stack = [package]
    while package_stack:
        current_package = package_stack.pop()
        total_version_sum += current_package.version
        for p in current_package.sub_packages:
            package_stack.append(p)

    print(f'Total sum of versions: {total_version_sum}')

    print(f'Value of outer most package: {package.calculate_package()}')


if __name__ == '__main__':
    parse_file()
