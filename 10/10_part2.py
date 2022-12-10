with open("example.txt") as file:
    example_input = [l.strip() for l in file.readlines()]

with open("input.txt") as file:
    real_input = [l.strip() for l in file.readlines()]


def draw_pixel(x, cycle):
    to_check = x+1
    if to_check - 1 <= cycle % 40 <= to_check + 1:
        print("#", end="")
    else:
        print(".", end="")


def run(input):
    total = 0
    x = 1
    cycle = 0
    i = 0
    while len(input) > i:
        cycle += 1
        was_adding = False
        # Cycle starts
        if cycle % 40 == 0:
            print()
        draw_pixel(x, cycle)
        try:
            current_instruction = input[i]
            if current_instruction == "noop":
                pass
            elif current_instruction.startswith("addx"):
                was_adding = True
                cycle += 1
                if cycle % 40 == 0:
                    print()
                draw_pixel(x, cycle)
        except IndexError:
            pass

        # Cycle ends
        if was_adding:
            x += int(current_instruction.split(" ")[1])
        i += 1





run(example_input)
run(real_input)
