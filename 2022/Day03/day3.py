def sum_of_priorities():
    total_sum = 0

    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            first_comp, second_comp = line[:len(line)//2], line[len(line)//2:]

            for char in first_comp:
                if char in second_comp:
                    if char.isupper():  # Use ASCII to easily get the right value
                        total_sum += (ord(char) - 38)  # "A" should have value 27
                    else:
                        total_sum += (ord(char) - 96)  # "a" should have value 0
                    break

    return total_sum


def find_sum_of_badges():
    total_sum = 0
    lines = []

    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            lines.append(line)

    for i in range(0, len(lines), 3):
        for char in lines[i]:
            if char in lines[i+1] and char in lines[i+2]:
                if char.isupper():  # Use ASCII to easily get the right value
                    total_sum += (ord(char) - 38)  # "A" should have value 27
                else:
                    total_sum += (ord(char) - 96)  # "a" should have value 0
                break

    return total_sum


if __name__ == '__main__':
    print("The total sum of the priorities of items is: " + str(sum_of_priorities()))
    print("The total sum of the priorities of badge items is: " + str(find_sum_of_badges()))


