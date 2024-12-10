def is_safe(report):
    curr = int(report[0])
    mode = ""
    safe = True
    for i in report[1:]:
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
        if not 1 <= abs(i - curr) <= 3:
            safe = False
            break
        curr = i
    return safe


def additional_rule(report):
    report = report.split()

    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1:]):
            return True
    return False


safe_reports = 0
with open("input.txt") as file:
    for line in file.readlines():
        safe_reports += additional_rule(line)
print(safe_reports)
