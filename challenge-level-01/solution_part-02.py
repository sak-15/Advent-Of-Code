# Function to calculate the similarity score
def calculate_similarity_score(cordinates1, cordinates2):
    dic = dict()
    for i in cordinates2:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    
    similarity_score = 0

    for j in cordinates1:
        if j in dic.keys():
            similarity_score += j * dic[j]
        
    return similarity_score

# Initialize both the cordinates lists
cordinates1 = []
cordinates2 = []

# Read the input from the file
with open("input.txt", 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        cordinates1.append(left)
        cordinates2.append(right)

print(calculate_similarity_score(cordinates1, cordinates2))