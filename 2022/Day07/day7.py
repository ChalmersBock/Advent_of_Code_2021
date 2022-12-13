from collections import deque


class Tree:
    def __init__(self, value, name):
        self.children = []
        self.name = name
        self.value = value
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_child_with_name(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def get_total_value(self):
        if not self.children:
            return self.value
        total = 0
        for child in self.children:
            total += child.get_total_value()
        return total


def build_directory_tree():
    root = None
    init = True
    tree_pos = None
    commands = deque()

    with open("data", "r", encoding='utf-8') as file:
        for line in [line.strip() for line in file.readlines()]:
            commands.append(line)

    while commands:
        line = commands.popleft()
        if init:
            _, name = line.split("cd")
            root = Tree(0, name.strip())
            tree_pos = root
            init = False
        elif line == "$ cd ..":
            tree_pos = tree_pos.get_parent()
        elif line[0:4] == "$ cd":
            _, name = line.split(" cd ")
            tree_pos = tree_pos.get_child_with_name(name.strip())
        elif line[0:4] == "$ ls":
            while commands and commands[0][0] != "$":
                line = commands.popleft()
                if line[0:3] == "dir":
                    _, name = line.split(" ")
                    node = Tree(0, name.strip())
                    tree_pos.add_child(node)
                else:
                    value, name = line.split(" ")
                    node = Tree(int(value), name.strip())
                    tree_pos.add_child(node)
    return root


def sum_of_directories():
    valid_totals = []
    root = build_directory_tree()
    stack = deque()
    stack.append(root)

    while stack:
        item = stack.pop()
        if item.value == 0:
            for child in item.get_children():
                stack.append(child)
            total = item.get_total_value()
            if total <= 100000:
                valid_totals.append(total)

    print("The sum of the directories is: " + str(sum(valid_totals)))


def free_up_space(available, needed):
    valid_totals = []
    root = build_directory_tree()
    free_space = available - root.get_total_value()
    min_size = needed - free_space

    stack = deque()
    stack.append(root)

    while stack:
        item = stack.pop()
        if item.value == 0:
            for child in item.get_children():
                stack.append(child)
            total = item.get_total_value()
            if total >= min_size:
                valid_totals.append(total)

    print("The size of the directory is: " + str(min(valid_totals)))


if __name__ == '__main__':
    sum_of_directories()
    free_up_space(70000000, 30000000)
