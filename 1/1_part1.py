with open("input.txt") as file:
    lines = []
    for line in file:
        try:
            lines.append(int(line))
        except ValueError:
            lines.append(-1)

max = 0
curr_sum = 0
for i in lines:
    if i == -1:
        curr_sum = 0
    else:
        curr_sum += i
    max = curr_sum if curr_sum > max else max

print(max)
