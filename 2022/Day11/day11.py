from collections import deque


class Monkey:
    def __init__(self, name, divide_worry):
        self.name = name
        self.divide_worry = divide_worry
        self.true_pass = -1
        self.false_pass = -1
        self.operation = ""
        self.operand = -1
        self.test = -1
        self.items = []
        self.other_monkeys = []
        self.inspections = 0

    def add_item(self, item):
        self.items.append(item)

    def check_items(self):

        for item in self.items:
            self.inspections += 1
            if self.operand == "old":
                operand = item
            else:
                operand = int(self.operand)

            if self.operation == "*":
                item = (item * operand)
            elif self.operation == "+":
                item = (item + operand)

            if self.divide_worry:  # Stress managed by specification from task
                item = item // 3
            else:  # We have to manage stress anyway, use the prime numbers from all monkeys to not affect divisibility
                mod = self.test
                for monkey in self.other_monkeys:
                    mod *= monkey.test
                item = item % mod

            if item % self.test != 0:
                self.other_monkeys[self.false_pass].items.append(item)
            else:
                self.other_monkeys[self.true_pass].items.append(item)
        self.items = []


def parse_monkeys(divide_worry):
    commands = deque()
    monkeys = []

    with open("data", "r", encoding='utf-8') as file:
        for line in [line.strip() for line in file.readlines()]:
            commands.append(line)

    while commands:
        line = commands.popleft()
        if line[0:6] == "Monkey":
            _, name = line.split(" ")
            monkey = Monkey(name[:-1], divide_worry)
            while commands and commands[0]:
                line = commands.popleft()
                if "Starting items:" in line:
                    _, items_string = line.split(":")
                    items = [int(x.strip()) for x in items_string.split(",")]
                    monkey.items = items
                elif "Operation:" in line:
                    _, operation_operand = line.split("old", 1)
                    operation, operand = operation_operand.strip().split(" ")
                    monkey.operation = operation
                    monkey.operand = operand
                elif "Test" in line:
                    _, test = line.split("by ")
                    monkey.test = int(test)
                elif "If true" in line:
                    _, true_monkey = line.split("monkey ")
                    monkey.true_pass = int(true_monkey)
                elif "If false" in line:
                    _, false_monkey = line.split("monkey ")
                    monkey.false_pass = int(false_monkey)
            monkeys.append(monkey)

    for monkey in monkeys:
        monkey.other_monkeys = monkeys

    return monkeys


def calculate_monkey_business(rounds, divide_worry):
    monkeys = parse_monkeys(divide_worry)

    for i in range(0, rounds):
        for monkey in monkeys:
            monkey.check_items()

    total_inspections = []
    for monkey in monkeys:
        total_inspections.append(monkey.inspections)

    total_inspections.sort(reverse=True)
    return total_inspections[0] * total_inspections[1]


if __name__ == '__main__':
    print("(Part 1) Total Monkey Business is: ", calculate_monkey_business(20, True))
    print("(Part 2) Total Monkey Business is: ", calculate_monkey_business(10000, False))
