import re

# Extracting the numbers from the input
def extract_numbers(data):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    control_pattern = r"(do\(\)|don't\(\))"
    matches = re.findall(f"{control_pattern}|{pattern}",data)
    return matches

with open('input3.txt', 'r') as file:
    data = file.read()

matches = extract_numbers(data)
sum = 0
mul_enabled = True
for match in matches:
    if match[0]:
        if match[0] == "do()":
            mul_enabled = True
        elif match[0] == "don't()":
            mul_enabled = False
    elif match[1] and match[2]:
        if mul_enabled:
            x, y = int(match[1]), int(match[2])
            sum += x * y

print(sum)