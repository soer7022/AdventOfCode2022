import os
import sys
import time

height_map = []
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        height_map.append([x for x in line])

current_char = "a"
current_pos = (0, 0)
goal = (0, 0)
for i in range(0, len(height_map)):
    for j in range(0, len(height_map[i])):
        if height_map[i][j] == "S":
            current_pos = (i, j)
            height_map[i][j] = "a"
        elif height_map[i][j] == "E":
            goal = (i, j)
            height_map[i][j] = "z"
print(current_pos, goal)


def print_path(path, visited):
    time.sleep(0.001)
    print("\033[0;0H")
    for i in range(0, len(height_map)):
        for j in range(0, len(height_map[i])):
            if (i, j) == current_pos:
                print("\033[94m#\33[0m", end="")
            elif (i, j) == goal:
                print("\033[92mG\33[0m", end="")
            elif (i, j) in path:
                print("\033[94m.\33[0m", end="")
            elif (i, j) in visited:
                print("\033[32m" + height_map[i][j] + "\33[0m", end="")
            else:
                print('\33[0m' + height_map[i][j] + "\33[0m", end="")
        print()


def bfs(starting_point):
    queue = []
    visited = set()
    queue.append(([], starting_point))
    visited.add(starting_point)
    while len(queue) > 0:
        prev, current_pos = queue.pop(0)
        current_char = height_map[current_pos[0]][current_pos[1]]

        if current_pos == goal:
            print_path(prev, visited)
            return len(prev)
        # check down and up from current position
        for i in range(-1, 2):
            if i == 0:
                continue
            if current_pos[0] + i < 0 or current_pos[0] + i >= len(height_map):
                continue
            if (
                    height_map[current_pos[0] + i][current_pos[1]] <= current_char
                    or ord(height_map[current_pos[0] + i][current_pos[1]])
                    == ord(current_char) + 1
            ):
                if (current_pos[0] + i, current_pos[1]) not in visited:
                    queue.append((prev + [current_pos], (current_pos[0] + i, current_pos[1])))
                    visited.add((current_pos[0] + i, current_pos[1]))

        # check left and right from current position
        for i in range(-1, 2):
            if i == 0:
                continue
            if current_pos[1] + i < 0 or current_pos[1] + i >= len(height_map[0]):
                continue
            if (
                    height_map[current_pos[0]][current_pos[1] + i] <= current_char
                    or ord(height_map[current_pos[0]][current_pos[1] + i])
                    == ord(current_char) + 1
            ):
                if (current_pos[0], current_pos[1] + i) not in visited:
                    queue.append((prev + [current_pos], (current_pos[0], current_pos[1] + i)))
                    visited.add((current_pos[0], current_pos[1] + i))


best = 10000000000
for i in range(0, len(height_map)):
    for j in range(0, len(height_map[i])):
        if height_map[i][j] == "a":
            try:
                best = min(best, bfs((i, j)))
            except TypeError:
                pass
print(best)
