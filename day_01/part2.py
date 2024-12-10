first_line = []
second_line = []
with open("input.txt") as file:
    for line in file.readlines():
        first_line.append(line.split()[0])
        second_line.append(line.split()[1])
first_line = sorted(first_line)
second_line = sorted(second_line)

similarity_score = 0
for i in first_line:
    similarity_score += int(i) * len([x for x in second_line if x == i])
print(similarity_score)
