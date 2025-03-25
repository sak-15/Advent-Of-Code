import re

# Extracting the numbers from the input
def extract_numbers(data):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, data)
    return matches

with open('input3.txt', 'r') as file:
    data = file.read()

sum = 0
matches = extract_numbers(data)
for a,b in matches:
    sum+=int(a)*int(b)

print(sum)