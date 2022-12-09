def update_t_pos(h_pos, t_pos):
    x_diff = h_pos[0] - t_pos[0]
    y_diff = h_pos[1] - t_pos[1]
    x_change = 0
    y_change = 0

    if x_diff > 1 or (x_diff == 1 and abs(y_diff) > 1):
        x_change = 1
    elif x_diff < -1 or (x_diff == -1 and abs(y_diff) > 1):
        x_change = -1
    if y_diff > 1 or (y_diff == 1 and abs(x_diff) > 1):
        y_change = 1
    elif y_diff < -1 or (y_diff == -1 and abs(x_diff) > 1):
        y_change = -1

    return t_pos[0] + x_change, t_pos[1] + y_change


def determine_direction(direction):
    if direction == "R":
        return 1, 0
    elif direction == "L":
        return -1, 0
    elif direction == "U":
        return 0, 1
    elif direction == "D":
        return 0, -1
    return 0, 0


def calculate_visits_for_tail():
    moves = []

    with open("data", "r", encoding='utf-8') as file:
        for line in [line.strip() for line in file.readlines()]:
            direction, steps = line.split(" ")
            moves.append(
                {
                    "dir": direction,
                    "steps": int(steps)
                }
            )

    t_pos = (0, 0)
    h_pos = (0, 0)
    visited_pos = {(0, 0)}

    for move in moves:
        x_change, y_change = determine_direction(move["dir"])

        for i in range(move["steps"]):
            h_pos = (h_pos[0] + x_change, h_pos[1] + y_change)
            t_pos = update_t_pos(h_pos, t_pos)
            visited_pos.add(t_pos)

    return len(visited_pos)


if __name__ == '__main__':
    print("Tail has visited:", str(calculate_visits_for_tail()), "spots")

