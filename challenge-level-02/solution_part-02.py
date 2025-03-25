# Checks if list is strictly increasing
def is_strictly_increasing(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1] or list[i+1]-list[i]>3 or list[i+1]-list[i]<1:
            return False
    return True

# Checks if list is strictly decreasing
def is_strictly_decreasing(list):
    for i in range(len(list) - 1):
        if list[i] < list[i + 1] or list[i]-list[i+1]>3 or list[i]-list[i+1]<1:
            return False
    return True

# Checks if the reports are safe
def is_safe(input):
    input = list(map(int, input.split()))
    if is_strictly_increasing(input) or is_strictly_decreasing(input):
        return True
    for i in range(len(input)):
        new_input = input[:i]+input[i+1:]
        if is_strictly_increasing(new_input) or is_strictly_decreasing(new_input):
            return True
    else:
        return False

# Read the input from file
with open('input2.txt', 'r') as file:
    data = file.readlines()

safe = 0
for report in data:
    if is_safe(report.strip()):
        safe += 1
    
print(safe)
