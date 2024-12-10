safe_reports = 0
with open("input.txt") as file:
    for line in file.readlines():
        curr = int(line.split()[0])
        mode = ""
        safe = True
        for i in line.split()[1:]:
            i = int(i)
            if i > curr:
                if mode == "":
                    mode = "A"
                if mode == "D":
                    safe = False
                    break
            elif i < curr:
                if mode == "":
                    mode = "D"
                if mode == "A":
                    safe = False
                    break
            if not 1 <= abs(i-curr) <= 3:
                safe = False
                break
            curr = i
        if safe:
            safe_reports += 1
print(safe_reports)