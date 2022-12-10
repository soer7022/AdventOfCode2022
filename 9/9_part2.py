with open("example.txt") as file:
    example_input = [line.strip() for line in file.readlines()]
with open("input.txt") as file:
    real_input = [line.strip() for line in file.readlines()]


def run(input):
    visited = set()
    H_pos = (0, 0)
    knots = [(0,0) for x in range(9)]
    print(knots)
    visited.add(knots[8])


    def position_tail(T_pos, H_pos):
        distance_horizontal = T_pos[0] - H_pos[0]
        distance_vertical = T_pos[1] - H_pos[1]
        if abs(distance_vertical)  + abs(distance_horizontal) >= 3:
            # diagonal move
            if distance_horizontal < 0:
                T_pos = (T_pos[0] + 1, T_pos[1])
            elif distance_horizontal > 0:
                T_pos = (T_pos[0] - 1, T_pos[1])

            if distance_vertical < 0:
                T_pos = (T_pos[0], T_pos[1] + 1)
            elif distance_vertical > 0:
                T_pos = (T_pos[0], T_pos[1] - 1)
        elif abs(distance_horizontal) > 1:
            # horizontal move
            if distance_horizontal < 0:
                T_pos = (T_pos[0] + 1, T_pos[1])
            else:
                T_pos = (T_pos[0] - 1, T_pos[1])
        elif abs(distance_vertical) > 1:
            # vertical move
            if distance_vertical < 0:
                T_pos = (T_pos[0], T_pos[1] + 1)
            else:
                T_pos = (T_pos[0], T_pos[1] - 1)

        return T_pos, H_pos

    for line in input:
        direction, count = line.split(" ")
        count = int(count)

        # move up
        for i in range(count):
            if direction == "U":
                H_pos = (H_pos[0], H_pos[1] + 1)
            elif direction == "D":
                H_pos = (H_pos[0], H_pos[1] - 1)
            elif direction == "L":
                H_pos = (H_pos[0] - 1, H_pos[1])
            elif direction == "R":
                H_pos = (H_pos[0] + 1, H_pos[1])
            for i in range(len(knots)):
                if i == 0:
                    knots[i], H_pos = position_tail(knots[i], H_pos)
                else:
                    knots[i], _ = position_tail(knots[i], knots[i-1])
            visited.add(knots[8])

    print(len(visited))




run(example_input)
run(real_input)
