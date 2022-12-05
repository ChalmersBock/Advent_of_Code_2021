def supply_stacks(vers_9001):
    h_stacks = []
    commands = []
    command_lines = False

    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            if not line.strip():  # Switch to parsing commands
                command_lines = True
            elif command_lines:  # Collect important info from commands
                line = line[4:].strip()
                c, ft = line.split("from")
                f, t = ft.split("to")
                temp = {
                    "crates": int(c),
                    "to": int(t) - 1,
                    "from": int(f) - 1
                }
                commands.append(temp)
            else:  # Create a horizontal stack
                line = line.rstrip()
                row = []
                for i in range(1, len(line), 4):
                    row.append(line[i:i+1])
                h_stacks.append(row)

    # Set up correct number of vertical stacks
    v_stacks = []
    numbers = h_stacks.pop()
    for i in range(len(numbers)):
        v_stacks.append([])
    h_stacks.reverse()

    # Turn the horizontal stacks into vertical stacks
    for i in range(len(h_stacks)):
        for j in range(len(h_stacks[i])):
            if h_stacks[i][j].strip():
                v_stacks[j].append(h_stacks[i][j])

    # Perform the commands on the vertical stacks
    if vers_9001:
        for command in commands:
            length = len(v_stacks[command["from"]])
            for i in range(length - command["crates"], length):
                v_stacks[command["to"]].append(
                    v_stacks[command["from"]].pop(length - command["crates"])
                )
    else:
        for command in commands:
            for i in range(command["crates"]):
                v_stacks[command["to"]].append(
                    v_stacks[command["from"]].pop()
                )

    string = ""
    for stack in v_stacks:
        string += stack.pop()

    print("The final top crates are: " + string)


if __name__ == '__main__':
    supply_stacks(False)
    supply_stacks(True)
