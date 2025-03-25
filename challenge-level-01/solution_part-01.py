def calculate_total_distance(cordinates1, cordinates2):
    cordinates1.sort()
    cordinates2.sort()
    total_distance = 0
    for i in range(len(cordinates1)):
        total_distance += abs(cordinates1[i] - cordinates2[i])
    return total_distance

cordinates1 = []
cordinates2 = []

with open("input.txt", 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        cordinates1.append(left)
        cordinates2.append(right)

print(calculate_total_distance(cordinates1, cordinates2))
