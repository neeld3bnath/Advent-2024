from sympy import *
# def get_file_data(file_name):
#     with open(file_name) as f:
#         data = f.read()
#         return data

def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def get_answer_1(data):
    with open(data) as f:
        data = f.readlines()
    table = []
    x, y = symbols("x y")
    result = 0
    for line in data:
        line = line.strip()
        if line.startswith("Button A"):
            table.append(line.split("+")[1].split(",")[0])
            table.append(line.split("+")[2])
        elif line.startswith("Button B"):
            table.append(line.split("+")[1].split(",")[0])
            table.append(line.split("+")[2])
        elif line.startswith("Prize"):
            table.append(line.split("X=")[1].split(",")[0])
            table.append(line.split("Y=")[1])
    table = [int(x) for x in table]
    for i in range(0, len(table)-5, 6):
        solver = solve((Eq(table[i]*table[i+2], table[i+4]), Eq(table[i+1]*table[i+3], table[i+5])), (x,y))
        if solver:
            result += int(solver[0])
    return result
    

# file_data = get_file_data("input13.txt")
print(f"The answer for part 1 is {get_answer_1("input13.txt")}")