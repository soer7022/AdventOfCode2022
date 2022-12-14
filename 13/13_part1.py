from ast import literal_eval

with open("input.txt") as file:
    example_pairs = []
    for line in file.read().split("\n\n"):
        a, b = line.split("\n")
        example_pairs.append((a, b))


def is_pair_valid(left, right):
    if type(left) == str:
        left = literal_eval(left)
        right = literal_eval(right)
    for i in range(max(len(left), len(right))):
        try:
            left[i]
        except IndexError:
            return True
        try:
            right[i]
        except IndexError:
            return False
        if type(left[i]) == list and type(right[i]) == int:
            right[i] = [right[i]]
        elif type(left[i]) == int and type(right[i]) == list:
            left[i] = [left[i]]
        if type(left[i]) == list and type(right[i]) == list:
            valid = is_pair_valid(left[i], right[i])
            if valid is None:
                continue
            else:
                return valid

        if left[i] == right[i]:
            continue
        elif left[i] > right[i]:
            return False
        else:
            return True


total = 0
for i in range(len(example_pairs)):
    print("Pair {}".format(i))
    valid = is_pair_valid(*example_pairs[i])
    if valid:
        total += (i + 1)
print(total)
