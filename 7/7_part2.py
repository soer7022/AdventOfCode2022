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
        command = line.split(" ")
        if line.startswith("$ cd"):
            if command[2] == "..":
                path.pop()
            elif command[2] == "/":
                path = ["/"]
            else:
                path += [command[2]]
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            dir_name = command[1]
            sizes["".join(path + [dir_name])] = 0
        else:
            sizes["".join(path)] += int(command[0])
            for i in range(1, len(path)):
                sizes["".join(path[:-i])] += int(command[0])

    unused_space = 70000000 - sizes["/"]
    space_to_find = 30000000 - unused_space
    for size in sorted(sizes.values()):
        if size >= space_to_find:
            return size


print(run(example_input))
print(run(real_input))
