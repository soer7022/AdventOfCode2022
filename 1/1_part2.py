with open('input.txt') as file:
    lines = []
    for line in file:
        try:
            lines.append(int(line))
        except ValueError:
            lines.append(-1)

scores = []
curr_sum = 0
for i in lines:
    if i == -1:
        scores.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += i

scores.sort()
print(scores[-1] + scores[-2] + scores[-3])