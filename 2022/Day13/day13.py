from collections import deque


def parse_list(stack):
    item = []
    current_string = ""

    while stack:
        c = stack.popleft()
        if c.isdigit():
            current_string += c
        elif c == "," and current_string != "":
            item.append(int(current_string))
            current_string = ""
        elif c == "[":
            item.append(parse_list(stack))
        elif c == "]":
            if current_string.isdigit():
                item.append(int(current_string))
            return item
    return item


def parse_pairs():
    pairs = []
    stack = deque()

    with open("data", "r", encoding='utf-8') as file:
        pair = []
        for line in [line.strip() for line in file.readlines()]:
            if not line:
                pairs.append(pair)
                pair = []
            else:
                for char in line:
                    stack.append(char)
                item = parse_list(stack)[0]
                pair.append(item)
        if pair:
            pairs.append(pair)
    return pairs


def check_list(left, right):
    for i in range(min(len(right), len(left))):
        l, r = left[i], right[i]
        if isinstance(r, list) and isinstance(l, list):
            result = check_list(l, r)
            if result is not None:
                return result
        elif isinstance(r, list):
            l_list = [l]
            result = check_list(l_list, r)
            if result is not None:
                return result
        elif isinstance(l, list):
            r_list = [r]
            result = check_list(l, r_list)
            if result is not None:
                return result
        else:
            if l < r:
                return True
            elif l > r:
                return False

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False


def check_pairs():
    total_sum = 0
    pairs = parse_pairs()
    for i in range(len(pairs)):
        left, right = pairs[i]
        if check_list(left, right):
            total_sum += i+1
    print("The sum of all the indexes for lists in the right order is: ", total_sum)


def bubble(packages):
    n = len(packages)
    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not check_list(packages[j], packages[j + 1]):
                swapped = True
                packages[j], packages[j + 1] = packages[j + 1], packages[j]
        if not swapped:
            return


def sort_packages():
    packages = sum(parse_pairs(), [])
    packages.extend([[[2]], [[6]]])
    bubble(packages)

    two_index = -1
    six_index = -1
    for i in range(len(packages)):
        if packages[i] == [[2]]:
            two_index = i + 1
        elif packages[i] == [[6]]:
            six_index = i + 1
    print("The decoder key is: ", two_index*six_index)


if __name__ == '__main__':
    check_pairs()
    sort_packages()
