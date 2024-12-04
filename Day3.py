import re

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def get_answer_1(data):
    total = 0
    for line in data:
        matches = re.findall(r'mul\((\d+),(\d+)\)', line)
        for match in matches:
            total += int(match[0]) * int(match[1])
    return total

def get_answer_2(data):
    total = 0
    enabled = True
    for line in data:
        dontsAndDos = re.findall(r'don\'t\(\)|do\(\)', line)
        if len(dontsAndDos) > 0:
            if dontsAndDos[-1] == 'don\'t()':
                enabled = False
            else:
                enabled = True
        if enabled:
            matches = re.findall(r'mul\((\d+),(\d+)\)', line)
            for match in matches:
                total += int(match[0]) * int(match[1])
    return total

    
file_data = get_file_data("input3.txt")

print(f"The answer for part 1 is {get_answer_1(file_data)}")
print(f"The answer for part 2 is {get_answer_2(file_data)}")