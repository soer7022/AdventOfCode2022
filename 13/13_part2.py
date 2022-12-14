import functools
from ast import literal_eval

with open("input.txt") as file:
    example_pairs = []
    for line in file.read().split("\n\n"):
        a, b = line.split("\n")
        example_pairs.append(a)
        example_pairs.append(b)
    example_pairs.append("[[2]]")
    example_pairs.append("[[6]]")


def is_pair_valid(left, right):
    if type(left) == str:
        left = literal_eval(left)
        right = literal_eval(right)
    for i in range(max(len(left), len(right))):
        try:
            left[i]
        except IndexError:
            return 1
        try:
            right[i]
        except IndexError:
            return -1
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
            return -1
        else:
            return 1


example_pairs.sort(key=functools.cmp_to_key(is_pair_valid))
example_pairs.reverse()
print((example_pairs.index("[[2]]") + 1) * (example_pairs.index("[[6]]") + 1))
