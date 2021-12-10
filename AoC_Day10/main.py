import os
import sys

match_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

value_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

value_dict_two = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def find_corruption():
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        errors = []
        non_corrupt_lines = []
        for line in file.readlines():
            stack = []
            line = line.strip()
            not_corrupt = True
            for char in line:
                if char in ['(', '[', '{', '<']:
                    stack.append(char)
                else:
                    match = stack.pop()
                    if match_dict[match] != char:
                        errors.append(char)
                        not_corrupt = False
                        break
            if not_corrupt:
                non_corrupt_lines.append(line)

    total_error_sum = 0
    for error in errors:
        total_error_sum += value_dict[error]
    print(f'Total error sum: {total_error_sum}')

    return non_corrupt_lines


def finish_lines(lines):
    score_list = []
    for line in lines:
        stack = []
        line = line.strip()
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                stack.pop()

        stack.reverse()
        line_sum = 0
        for char in stack:
            line_sum *= 5
            line_sum += value_dict_two[match_dict[char]]
        score_list.append(line_sum)
        print(f'Stack: {stack}, score: {line_sum}')

    score_list.sort()
    middle_index = int((len(score_list)-1)/2)
    print(f'Final score: {score_list[middle_index]}')



if __name__ == '__main__':
    no_corruption = find_corruption()
    finish_lines(no_corruption)


