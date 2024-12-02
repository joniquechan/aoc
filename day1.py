# read input from file
left_col = []
right_col = []

# create two arrays and put first number in first and second number in second
with open('day1.txt', 'r') as file:
    for line in file: 
        left, right = line.split()
        left_col.append(int(left))
        right_col.append(int(right))

# sort each array
left_col.sort()
right_col.sort()

# for loop for each element in array and find difference
difference = []
for left, right in zip(left_col, right_col):
    difference.append(abs(right - left))

# add total
total = 0
for diff in difference:
    total += diff

# dict(number, # count)
# iterate through dictionary and multiply key with value, add to total
count_dict = {}
for l in left_col:
    count = 0
    for r in right_col:
        if l == r:
            count += 1
    count_dict[l] = count

# similarity score
ss = 0
for key, value in count_dict.items():
    ss += key * value

print(f"{total} {ss}")