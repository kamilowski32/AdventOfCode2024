import re

sum = 0
with open("input.txt") as file:
    i = 0
    for line in file.readlines():
        regex = re.compile('mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)')
        matches = [m.groupdict() for m in regex.finditer(line)]
        for values in matches:
            sum += int(values["num1"]) * int(values["num2"])
print(sum)
