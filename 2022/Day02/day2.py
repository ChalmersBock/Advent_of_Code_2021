point_dict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

tactic_dict = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


def calculate_score(tactic):
    rounds = []
    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            rounds.append(line.strip())

    total_score = 0
    for r in rounds:
        if tactic:
            total_score += tactic_dict[r]
        else:
            total_score += point_dict[r]

    return total_score


if __name__ == '__main__':
    print("Score with misunderstanding: " + str(calculate_score(False)))
    print("Score with tactic: " + str(calculate_score(True)))
