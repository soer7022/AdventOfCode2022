with open("input.txt") as file:
    example_paths = [line.strip() for line in file.readlines()]

sand_start = (500, 0)

waterfall = {}


def draw_waterfall():
    start_x = min(waterfall.keys(), key=lambda x: x[0])[0]
    end_x = max(waterfall.keys(), key=lambda x: x[0])[0]
    start_y = min(waterfall.keys(), key=lambda x: x[1])[1]
    end_y = max(waterfall.keys(), key=lambda x: x[1])[1]
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if (x, y) in waterfall:
                print(waterfall[(x, y)], end="")
            else:
                print(".", end="")
        print()
    for x in range(start_x, end_x + 1):
        print("#", end="")
    print()


for path in example_paths:
    points = path.split(" -> ")
    for i in range(len(points) - 1):
        start_x, start_y = [int(p) for p in points[i].split(",")]
        end_x, end_y = [int(p) for p in points[i + 1].split(",")]

        if start_x == end_x:
            if start_y > end_y:
                for y in range(start_y, end_y - 1, -1):
                    waterfall[(start_x, y)] = "#"
            else:
                for y in range(start_y, end_y + 1):
                    waterfall[(start_x, y)] = "#"

        elif start_y == end_y:
            if start_x > end_x:
                for x in range(start_x, end_x - 1, -1):
                    waterfall[(x, start_y)] = "#"
            else:
                for x in range(start_x, end_x + 1):
                    waterfall[(x, start_y)] = "#"
highest_y = max([y for x, y in waterfall.keys()])
draw_waterfall()
finished = False
while not finished:
    currently_falling = True
    current_position = sand_start
    while currently_falling:
        if current_position[1] > highest_y:
            obstacle_below = "#"
            obstacle_below_left = "#"
            obstacle_below_right = "#"
        else:
            obstacle_below = waterfall.get((current_position[0], current_position[1] + 1))
            obstacle_below_left = waterfall.get((current_position[0] - 1, current_position[1] + 1))
            obstacle_below_right = waterfall.get((current_position[0] + 1, current_position[1] + 1))
        if obstacle_below is None:
            current_position = (current_position[0], current_position[1] + 1)
        elif obstacle_below_left is None:
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif obstacle_below_right is None:
            current_position = (current_position[0] + 1, current_position[1] + 1)
        else:
            waterfall[current_position] = "o"
            currently_falling = False
        if current_position == sand_start:
            currently_falling = False
            finished = True
            break

draw_waterfall()

count_o = 0
for key in waterfall.keys():
    if waterfall[key] == "o":
        count_o += 1
print(count_o)
