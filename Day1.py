def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

    
def get_answer_1(data):
    change = 0
    leftnums = []
    rightnums = []
    for line in data:
        numbers = line.split("   ")
        leftnum = int(numbers[0])
        rightnum = int(numbers[1])
        leftnums.append(leftnum)
        rightnums.append(rightnum)
    leftnums.sort()
    rightnums.sort()
    for i in range(len(leftnums)):
        change += abs(leftnums[i] - rightnums[i])
    return change
    
def get_answer_2(data):
    simScore = 0
    leftnums = []
    rightnums = []
    for line in data:
        numbers = line.split("   ")
        leftnum = int(numbers[0])
        rightnum = int(numbers[1])
        leftnums.append(leftnum)
        rightnums.append(rightnum)
    for i in range(len(leftnums)):
        count = rightnums.count(leftnums[i])
        simScore += count * leftnums[i]
    return simScore

file_data = get_file_data("input1.txt")

print(f"The answer for part 1 is {get_answer_1(file_data)}")
print(f"The answer for part 2 is {get_answer_2(file_data)}")


