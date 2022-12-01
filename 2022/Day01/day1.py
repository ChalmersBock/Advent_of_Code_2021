def most_calories(number):
    calories = 0
    elf_calories = []

    with open("data", "r", encoding='utf-8') as file:
        for line in file.readlines():
            if line.strip():
                calories += int(line)
            else:
                elf_calories.append(calories)
                calories = 0
        if calories != 0:
            elf_calories.append(calories)

    elf_calories.sort(reverse=True)

    total = 0
    for i in range(0, number):
        total += elf_calories[i]

    return total


if __name__ == '__main__':
    print("Elf that has the most calories has: " + str(most_calories(1)))
    print("Top three elfs that have the most calories total have: " + str(most_calories(3)))
