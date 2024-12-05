import re

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def get_answer_1(data):
    total = 0
    # Convert data to a 2D grid
    grid = []
    max_length = max(len(line) for line in data)
    for line in data:
        # Pad shorter lines with spaces to make a rectangular grid
        grid.append(line.ljust(max_length))
    
    # Helper function to check if a string contains XMAS (forward or backward)
    def check_pattern(s):
        count = 0
        # Forward check
        count += s.count("XMAS")
        # Backward check
        count += s.count("SAMX")
        return count
    
    # Check horizontal patterns (including backwards)
    for line in grid:
        total += check_pattern(line)
    
    # Check vertical patterns
    for j in range(len(grid[0])):
        vertical = ''.join(grid[i][j] for i in range(len(grid)))
        total += check_pattern(vertical)
    
    # Check diagonals
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check diagonal right-down
            if i <= len(grid) - 4 and j <= len(grid[0]) - 4:
                diagonal = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
                total += check_pattern(diagonal)
            
            # Check diagonal left-down
            if i <= len(grid) - 4 and j >= 3:
                diagonal = grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3]
                total += check_pattern(diagonal)
    
    return total

file_data = get_file_data("input4.txt")

print(f"The answer for part 1 is {get_answer_1(file_data)}")