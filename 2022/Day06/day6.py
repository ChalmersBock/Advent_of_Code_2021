def find_marker_index(marker_length):
    with open("data", "r", encoding='utf-8') as file:
        line = file.readline()

    for i in range(marker_length, len(line)):
        chars = line[i-marker_length:i]
        if len(set(chars)) == len(chars):
            return str(i)
    return "-1"


if __name__ == '__main__':
    print("The start-of-packet marker is found after " + find_marker_index(4) + " characters.")
    print("The message marker is found after " + find_marker_index(14) + " characters.")
