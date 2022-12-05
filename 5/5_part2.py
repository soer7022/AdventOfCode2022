with open("input.txt") as file:
    text = file.read()
    initial_state, instructions = text.split("\n\n")

stacks = [[] for _ in range(9)]
for line in reversed(initial_state.split("\n")[:-1]):
    for index, box in enumerate(line[1::4]):
        if box != " ":
            stacks[index].append(box)

for instruction in instructions.split("\n"):
    _, count, _, from_stack, _, to_stack = instruction.split(" ")
    to_move = []
    for i in range(int(count)):
        to_move.append(stacks[int(from_stack) - 1].pop())
    stacks[int(to_stack) - 1] += reversed(to_move)

final_string = ""
for stack in stacks:
    final_string += stack.pop() if stack else " "
print(final_string)
