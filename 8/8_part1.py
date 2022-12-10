with open("example.txt") as file:
    example_input = [l.strip() for l in file.readlines()]

with open("input.txt") as file:
    real_input = [l.strip() for l in file.readlines()]


def run(input):
    max_score = 0
    width = len(input[0])
    height = len(input)
    for i in range(1, height - 1):
        for j in range(1,width - 1):
            current_height = input[i][j]
            # look at trees to the left
            clearance_left = 1
            for k in range(j - 1, 0, -1):
                if input[i][k] < current_height:
                    clearance_left += 1
                else:
                    break
            # look at trees to the right
            clearance_right = 1
            for k in range(j + 1, width-1):
                if input[i][k] < current_height:
                    clearance_right += 1
                else:
                    break
            # look at trees above
            clearance_up = 1
            for k in range(i - 1, 0, -1):
                if input[k][j] < current_height:
                    clearance_up += 1
                else:
                    break
            # look at trees below
            clearance_down = 1
            for k in range(i + 1, height-1):
                if input[k][j] < current_height:
                    clearance_down += 1
                else:
                    break
            score = clearance_down * clearance_left * clearance_right * clearance_up
            if score > max_score:
                max_score = score


    return max_score






print(run(example_input))

print(run(real_input))
