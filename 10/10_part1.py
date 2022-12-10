with open("example.txt") as file:
    example_input = [l.strip() for l in file.readlines()]

with open("input.txt") as file:
    real_input = [l.strip() for l in file.readlines()]


def get_strength(x, cycle):
    return x * cycle


def run(input):
    total = 0
    x = 1
    cycle = 0
    i = 0
    while cycle <= 220 and i < len(input):
        cycle += 1
        was_adding = False
        # Cycle starts
        if (cycle - 20) % 40 == 0:
            total += get_strength(x, cycle)
        current_instruction = input[i]
        if current_instruction == "noop":
            pass
        elif current_instruction.startswith("addx"):
            was_adding = True
            cycle += 1
            if (cycle - 20) % 40 == 0:
                total += get_strength(x, cycle)

        # Cycle ends
        if was_adding:
            x += int(current_instruction.split(" ")[1])
        i += 1

    return x, cycle, total


print(run(example_input))
print(run(real_input))
