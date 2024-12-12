def find_area(file:str):
    characters = set([char for char in file if char.isalpha()])
    print(characters)
    area = []
    area.append(file.count(char) for char in characters)
    return area

with open("input12.txt") as f:
    file = f.read()
    print(area for area in find_area(file))