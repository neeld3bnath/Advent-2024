def get_answer_1(data):
    data = data.split(" ")
    data = [x for x in data]
    for _ in range(25):
        new_data = []
        for j in range(len(data)):
            if data[j] == '0':
                new_data.append('1')
            elif len(data[j]) % 2 == 0:
                mid = len(data[j]) // 2
                left = str(int(data[j][:mid]))
                right = str(int(data[j][mid:]))
                new_data.append(left)
                new_data.append(right)
            else:
                new_data.append(str(int(data[j]) * 2024))
        data = new_data
    return len(data)

input_file = open("input11.txt", "r").read()
print(get_answer_1(input_file))