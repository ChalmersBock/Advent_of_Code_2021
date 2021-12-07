import os
import sys
import math
from numpy import median


def calculate_crab_fuel_median(crab_positions):

    goal_pos = int(round(median(crab_positions)))
    fuel_usage = 0

    for crab_pos in crab_positions:
        fuel_usage += abs(crab_pos-goal_pos)

    print(f'Fuel Usage Q1: {fuel_usage}')


def calculate_crab_fuel_average(crab_positions):

    goal_pos_above = int(math.ceil(sum(crab_positions)/len(crab_positions)))
    goal_pos_below = int(math.floor(sum(crab_positions)/len(crab_positions)))

    fuel_usage_above = 0
    fuel_usage_below = 0

    for crab_pos in crab_positions:
        for fuel_spent in range(abs(crab_pos - goal_pos_above) + 1):
            fuel_usage_above += fuel_spent
        for fuel_spent in range(abs(crab_pos - goal_pos_below) + 1):
            fuel_usage_below += fuel_spent

    best_choice = fuel_usage_above
    if fuel_usage_above > fuel_usage_below:
        best_choice = fuel_usage_below

    print(f'Fuel Usage Q2: {best_choice}')


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "data2"), "r", encoding='utf-8') as file:
        positions = list(map(int, file.read().split(",")))

    calculate_crab_fuel_median(positions)
    calculate_crab_fuel_average(positions)


