with open("input.txt") as file:
    example_monkeys = [line.strip() for line in file.read().split("\n\n")]


class Monkey:
    def __init__(self, number, items, operation, test, true_throw_to, false_throw_to):
        self.number = number
        self.items = items
        self.operation = operation
        self.test_divisible_by = test
        self.true_throw_to = true_throw_to
        self.false_throw_to = false_throw_to
        self.inspects = 0

    def take_turn(self, monkeys):
        while self.items:
            self.inspects += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item = item // 3
            if item % self.test_divisible_by == 0:
                monkeys[self.true_throw_to].items.append(item)
            else:
                monkeys[self.false_throw_to].items.append(item)

    def __repr__(self):
        return f"Monkey {self.number}:({self.items}, {self.operation}, {self.test_divisible_by}, {self.true_throw_to}, {self.false_throw_to})"


monkey_list = []


def name_func(name, operation_str):
    if "old" in operation_str:
        op = operation_str.split(" ")[0]

        def operation(x):
            return eval(f"{x} {op} {x}")

    else:

        def operation(x):
            return eval(f"{x} {operation_str}")

    operation.__name__ = name
    return operation


for monkey in example_monkeys:
    monkey = monkey.split("\n")
    monkey_number = int(monkey[0].split(" ")[1][:-1])
    items = [int(item) for item in monkey[1].split(": ")[1].split(", ")]
    operation_str = monkey[2].split(": ")[1].split("old ")[1]

    operation = name_func(f"operation_{monkey_number}", operation_str)
    test = int(monkey[3].split(": ")[1].split("divisible by ")[1])
    true_throw_to = int(monkey[4].split(": ")[1].split("throw to monkey ")[1])
    false_throw_to = int(monkey[5].split(": ")[1].split("throw to monkey ")[1])
    monkey_list.append(
        Monkey(monkey_number, items, operation, test, true_throw_to, false_throw_to)
    )

for i in range(20):
    for monkey in monkey_list:
        monkey.take_turn(monkey_list)

inspects = [monkey.inspects for monkey in monkey_list]
inspects.sort()
print(inspects[-1] * inspects[-2])
