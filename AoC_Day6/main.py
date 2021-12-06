import os
import sys


def lanternfish_growth(nbr_days):
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        start_fish = file.readline().split(",")

        fish_timer = {}
        for key in range(9):
            fish_timer[key] = 0

        for fish in start_fish:
            fish_timer[int(fish)] += 1

    for _ in range(nbr_days):
        reset = fish_timer[0]
        for key in range(6):
            fish_timer[key] = fish_timer[key+1]
        fish_timer[6] = fish_timer[7] + reset
        fish_timer[7] = fish_timer[8]
        fish_timer[8] = reset

    print(f'After {nbr_days} days: {sum(fish_timer.values())}')


if __name__ == '__main__':
    lanternfish_growth(80)
    lanternfish_growth(256)


