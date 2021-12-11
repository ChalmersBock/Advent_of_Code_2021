from collections import deque


def count_increase(block_size):
    counter = 0
    queue = deque()

    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            new_value = int(line)
            if len(queue) < block_size:
                queue.append(new_value)
            else:
                old_depth = sum(queue)
                queue.append(new_value)
                queue.popleft()
                new_depth = sum(queue)
                if new_depth > old_depth:
                    counter += 1

    print(f'With block_size: {block_size} the answer is: {counter}')


if __name__ == '__main__':
    count_increase(1)
    count_increase(3)
