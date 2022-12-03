letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as file:
    ruck_sacks = [line.strip() for line in file.readlines()]


def get_ruck_sack_matches(ruck_sacks: list):
    letters_seen1 = set(ruck_sacks[0])
    letters_seen2 = set(ruck_sacks[1])
    letters_seen3 = set(ruck_sacks[2])
    matching_letter = (
        letters_seen1.intersection(letters_seen2).intersection(letters_seen3).pop()
    )
    return list(letters).index(matching_letter) + 1


sum = 0
for ruck_sack in range(0, len(ruck_sacks), 3):
    sum += get_ruck_sack_matches(ruck_sacks[ruck_sack : ruck_sack + 3])

print(sum)
