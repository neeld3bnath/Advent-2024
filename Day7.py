import re
from itertools import product

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def eval_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        else:
            result *= numbers[i + 1]
    return result

def can_make_test_value(test_value, numbers):
    num_operators = len(numbers) - 1
    possible_operators = list(product(['+', '*'], repeat=num_operators))
    
    for operators in possible_operators:
        if eval_expression(numbers, operators) == test_value:
            return True
    return False

def get_answer_1(data):
    total = 0
    for line in data:
        test_part, nums_part = line.split(":")
        test_value = int(test_part)
        numbers = []
        for x in nums_part.split():
            if x.strip():
                numbers.append(int(x))
        
        if can_make_test_value(test_value, numbers):
            total += test_value
    
    return total

file_data = get_file_data("input7.txt")
result = get_answer_1(file_data)
print(f"Part 1 Answer: {result}")