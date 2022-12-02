# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors


def get_weapon(letter):
    if letter == "A" or letter == "X":
        return "Rock"
    elif letter == "B" or letter == "Y":
        return "Paper"
    elif letter == "C" or letter == "Z":
        return "Scissors"


def get_points(opponent, you):
    base_points = 0
    you = get_weapon(you)
    opponent = get_weapon(opponent)
    if you == "Rock":
        base_points += 1
    elif you == "Paper":
        base_points += 2
    elif you == "Scissors":
        base_points += 3

    if opponent == "Rock" and you == "Paper":
        base_points += 6
    elif opponent == "Paper" and you == "Scissors":
        base_points += 6
    elif opponent == "Scissors" and you == "Rock":
        base_points += 6
    elif opponent == you:
        base_points += 3
    return base_points


total_points = 0
with open("input.txt") as file:
    for line in file.readlines():
        line_split = line.split(" ")
        total_points += get_points(line_split[0], line_split[1].strip())

print(total_points)
