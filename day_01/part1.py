first_line = []
second_line = []
with open("input.txt") as file:
    for line in file.readlines():
        first_line.append(line.split()[0])
        second_line.append(line.split()[1])
first_line = sorted(first_line)
second_line = sorted(second_line)

sum_abs = 0
for i in range(len(first_line)):
    sum_abs += abs(int(first_line[i]) - int(second_line[i]))
print(sum_abs)