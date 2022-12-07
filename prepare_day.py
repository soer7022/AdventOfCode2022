import os
from pathlib import Path

import requests

day_no = input("Which day? would you like to prepare? ")
day_no = int(day_no)

with open("token") as file:
    token = file.read().strip()

try:
    os.mkdir(f"{day_no}")
except FileExistsError:
    print("Day already exists")
    quit()


Path(f"{day_no}/{day_no}_part1.py").touch()
Path(f"{day_no}/{day_no}_part2.py").touch()
Path(f"{day_no}/example.txt").touch()

import os

url = "https://adventofcode.com/2022/day/"+str(day_no)+"/input"
headers = {'Cookie': 'session='+token}
r = requests.get(url, headers=headers)

with open(f"{day_no}/input.txt", "w") as file:
    file.write(r.text.strip())

print("Done, happy hacking!")