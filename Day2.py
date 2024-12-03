def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def get_answer_1(data):
    safe = 0
    for line in data:
        numbers = [int(x) for x in line.split(" ")]
        is_safe = True
        
        # Check if sequence is strictly increasing or decreasing
        is_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1))
        is_decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers)-1))
        
        # Check if differences are between 1 and 3
        valid_differences = all(1 <= abs(numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers)-1))
        
        if (is_increasing or is_decreasing) and valid_differences:
            safe += 1
            
    return safe


def is_sequence_safe(numbers):
    if len(numbers) < 2:
        return True
        
    # Check if sequence is strictly increasing or decreasing
    is_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1))
    is_decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers)-1))
    
    # Check if differences are between 1 and 3
    valid_differences = all(1 <= abs(numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers)-1))
    
    return (is_increasing or is_decreasing) and valid_differences

def get_answer_2(data):
    safe = 0
    for line in data:
        numbers = [int(x) for x in line.split(" ")]
        
        # First check if it's safe without removing any number
        if is_sequence_safe(numbers):
            safe += 1
            continue
            
        for i in range(len(numbers)):
            # Try removing the number at position i
            test_numbers = numbers[:i] + numbers[i+1:]
            
            if is_sequence_safe(test_numbers):
                safe += 1
                break
                
    return safe

file_data = get_file_data("input2.txt")

print(f"The answer for part 1 is {get_answer_1(file_data)}")
print(f"The answer for part 2 is {get_answer_2(file_data)}")
