def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def get_answer_1(data):
    rules = []
    updates = []
    parsing_rules = True
    
    for line in data:
        if not line:
            parsing_rules = False
            continue
            
        if parsing_rules:
            left, right = line.split('|')
            rules.append((int(left), int(right)))
        else:
            updates.append([int(x) for x in line.split(',')])
    
    def is_valid_order(sequence, rules):
        seq_set = set(sequence)
        pos = {num: i for i, num in enumerate(sequence)}
        
        for before, after in rules:
            if before in seq_set and after in seq_set:
                if pos[before] > pos[after]:
                    return False
        return True
    
    total = 0
    for update in updates:
        if is_valid_order(update, rules):
            mid_idx = len(update) // 2
            total += update[mid_idx]
    
    return total


file_data = get_file_data("input5.txt")

print(f"The answer for part 1 is {get_answer_1(file_data)}")