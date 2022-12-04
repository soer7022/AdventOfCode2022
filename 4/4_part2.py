with open("input.txt") as file:
    pairs = [line.strip() for line in file.readlines()]


def has_overlap(pair):
    pair1, pair2 = pair.split(",")
    pair1_start = int(pair1.split("-")[0])
    pair1_end = int(pair1.split("-")[1])
    pair2_start = int(pair2.split("-")[0])
    pair2_end = int(pair2.split("-")[1])

    if pair1_start <= pair2_start <= pair1_end:
        return True
    elif pair2_start <= pair1_start <= pair2_end:
        return True
    else:
        return False


total = 0
for pair in pairs:
    if has_overlap(pair):
        total += 1

print(total)
