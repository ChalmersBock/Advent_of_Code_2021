def calculate_hydrothermal_vents(consider_diagonal):
    with open("data", "r", encoding='utf-8') as file:
        vent_lines = []

        for line in file.readlines():
            vent_line = {}
            line.strip()
            line.replace(" ", "")
            start, end = line.split("->")
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")

            vent_line["x1"] = int(x1)
            vent_line["x2"] = int(x2)
            vent_line["y1"] = int(y1)
            vent_line["y2"] = int(y2)

            vent_lines.append(vent_line)
            #print(vent_line)

    size = 1000
    ocean_floor = [ [0] * size for _ in range(size)]

    for vent in vent_lines:
        # The strides are used to travel either in positive or negative direction
        x_stride = 1
        y_stride = 1
        if vent["x1"] > vent["x2"]:
            x_stride = -1
        if vent["y1"] > vent["y2"]:
            y_stride = -1

        if vent["x1"] == vent["x2"] or vent["y1"] == vent["y2"]:
            for x_coord in range(vent["x1"], vent["x2"]+x_stride, x_stride):
                for y_coord in range(vent["y1"], vent["y2"]+y_stride, y_stride):
                    ocean_floor[x_coord][y_coord] += 1
        elif consider_diagonal:
            # Does not matter if we use x or y in for loop, should be same diff when used in range
            for index in range(abs(vent["x1"] - vent["x2"]) + 1):
                ocean_floor[vent["x1"] + x_stride*index][vent["y1"] + y_stride*index] += 1

    lines_overlap = 0
    for i in range(size):
        for j in range(size):
            if ocean_floor[i][j] >= 2:
                lines_overlap += 1

    if consider_diagonal:
        print(f'Answer Q2: {lines_overlap}')
    else:
        print(f'Answer Q1: {lines_overlap}')


if __name__ == '__main__':
    calculate_hydrothermal_vents(False)
    calculate_hydrothermal_vents(True)


