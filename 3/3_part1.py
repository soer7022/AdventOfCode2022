letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as file:
    ruck_sacks = [line.strip() for line in file.readlines()]


def get_ruck_sack_score(ruck_sack):
    seen_letters = set()
    matched_letters = set()
    score = 0
    compartment1, compartment2 = (
        ruck_sack[: len(ruck_sack) // 2],
        ruck_sack[len(ruck_sack) // 2 :],
    )
    for letter in compartment1:
        seen_letters.add(letter)
    for letter in compartment2:
        if letter in seen_letters:
            matched_letters.add(letter)
    for letter in matched_letters:
        score += list(letters).index(letter) + 1
    return score


sum = 0
for ruck_sack in ruck_sacks:
    sum += get_ruck_sack_score(ruck_sack)

print(sum)
