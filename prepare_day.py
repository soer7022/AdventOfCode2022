import os
from pathlib import Path

day_no = input("Which day? would you like to prepare? ")
day_no = int(day_no)

try:
    os.mkdir(f"{day_no}")
except FileExistsError:
    print("Day already exists")
    quit()

Path(f"{day_no}/input.txt").touch()
Path(f"{day_no}/{day_no}_part1.py").touch()
Path(f"{day_no}/{day_no}_part2.py").touch()

print("Done, happy hacking!")