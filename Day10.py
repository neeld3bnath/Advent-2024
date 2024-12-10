def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def can_grid_go_to_num(test_grid, num=0):
    count = 0
    if num == 9:
        return True
    for i in range(len(test_grid)):
        for j in range(len(test_grid[i])):
            if test_grid[i][j] == str(num):
                count += 1
                num += 1
                can_grid_go_to_num(test_grid, num)
    return count * 9


file_data = get_file_data("input10.txt")

# build a 2D List based on the file_data
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

print(f"The answer for part 1 is {can_grid_go_to_num(grid)}")
