import re

def parse_string(texts):
    value = 0
    for text in texts:
        regex = re.compile('mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)')
        matches = [m.groupdict() for m in regex.finditer(text)]
        for pairs in matches:
            value += int(pairs["num1"]) * int(pairs["num2"])
    return value

sum = 0
with open("input.txt") as file:
    file = file.read().replace("\n", "")
    regex1 = r"(.*?do)"
    start = [re.findall(regex1, file)[0]]
    sum += parse_string(start)


    regex2 = re.compile("(?P<all>do[^n][^d]*)")
    matches = [m.groupdict() for m in regex2.finditer(file)]
    rest = re.findall(regex2, file)
    sum += parse_string(rest)

print(sum)