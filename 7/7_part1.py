import sys
from functools import cache

with open("example.txt") as file:
    example_input = [l.strip() for l in file.readlines()]
with open("input.txt") as file:
    real_input = [l.strip() for l in file.readlines()]


def run(input):
    path = ["/"]
    sizes = {"/": 0}
    for line in input:
        if line.startswith("$"):
            command = line.split(" ")
            if line.startswith("$ cd"):
                if command[2] == "..":
                    path.pop()
                elif command[2] == "/":
                    path = ["/"]
                else:
                    path += [command[2]]
        elif line.startswith("dir"):
            dir_name = line.split(" ")[1]
            sizes["".join(path + [dir_name])] = 0
        else:
            sizes["".join(path)] += int(line.split(" ")[0])
            for i in range(1, len(path)):
                sizes["".join(path[:-i])] += int(line.split(" ")[0])

    sum = 0
    for value in sizes.values():
        if value <= 100000:
            sum += value
    return sum


print(run(example_input))
print(run(real_input))
