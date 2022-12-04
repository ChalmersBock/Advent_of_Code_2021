def completely_overlapping_sections():
    counter = 0

    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            first, second = line.split(",")
            start_f, end_f = first.split("-")
            start_s, end_s = second.split("-")

            if ((int(start_f) <= int(start_s) and int(end_f) >= int(end_s))
                    or (int(start_f) >= int(start_s) and int(end_f) <= int(end_s))):
                counter += 1

    return counter


def overlapping_sections():
    counter = 0

    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            first, second = line.split(",")
            start_f, end_f = first.split("-")
            start_s, end_s = second.split("-")

            if (int(start_s) <= int(start_f) <= int(end_s)
                    or int(start_s) <= int(end_f) <= int(end_s)
                    or int(start_f) <= int(start_s) <= int(end_f)
                    or int(start_f) <= int(end_s) <= int(end_f)):
                counter += 1

    return counter


if __name__ == '__main__':
    print("The number of completely overlapping sections are: " + str(completely_overlapping_sections()))
    print("The number of overlapping sections are: " + str(overlapping_sections()))

