with open("input.txt") as file:
    string_to_read = file.read().strip()

for i in range(len(string_to_read)):
    current_string = string_to_read[i:i+4]
    seen = set()
    found = False
    print(current_string)
    for char in current_string:
        if char in seen:
            found = True
        else:
            seen.add(char)
    if not found:
        print(i+4)
        break