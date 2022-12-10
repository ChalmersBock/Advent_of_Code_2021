def parse_actions():
    actions = []
    with open("data", "r", encoding='utf-8') as file:
        for line in [line.strip() for line in file.readlines()]:
            if line[0:4] == "addx":
                _, value = line.split(" ")
                actions.append({
                    "cycles": 2,
                    "value": int(value)
                })
            else:
                actions.append({
                    "cycles": 1,
                    "value": 0
                })
    return actions


def sum_of_signal_strengths():
    completed_cycles = 1
    pending_actions = parse_actions()
    x_value = 1
    signal_values = []

    for action in pending_actions:
        for cycle in range(action["cycles"]):
            if (completed_cycles + 20) % 40 == 0:
                signal_values.append(x_value * completed_cycles)
            if cycle == action["cycles"]-1:
                x_value += action["value"]
            completed_cycles += 1

    return sum(signal_values)


def draw_image():
    pending_actions = parse_actions()
    sprite_pos = 1
    drawing = []
    completed_cycles = 1

    for action in pending_actions:
        for cycle in range(action["cycles"]):
            if completed_cycles % 40 in [sprite_pos, sprite_pos+1, sprite_pos+2]:
                drawing.append("#")
            else:
                drawing.append(".")

            if cycle == action["cycles"]-1:
                sprite_pos += action["value"]

            if completed_cycles % 40 == 0:
                print("".join(i for i in drawing))
                drawing = []
            completed_cycles += 1


if __name__ == '__main__':
    print("The sum of the signal strengths are: " + str(sum_of_signal_strengths()))
    print("The output is the following: ")
    draw_image()
