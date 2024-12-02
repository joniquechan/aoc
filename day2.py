# parse input
# get each line
# increment safe_report if numbers in line are either ALL increasing/decreasing
# and adjacent levels differ by at least one and at most three

# check if sequence is safe
def safe(numbers):
    # calculate differences
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
    # check if every difference is in the range 1-3
    # increasing
    if all(1 <= diff <= 3 for diff in differences):
        return True
    # decreasing
    if all(-3 <= diff <= -1 for diff in differences):
        return True
    return False

# check  if sequence can be made safe
def can_be_safe(numbers):
    # remove each number and check if it is safe
    for i in range(len(numbers)):
        modified = numbers[:i] + numbers[i+1:]
        if safe(modified):
            return True
    return False

safe_report = 0
with open('day2.txt', 'r') as file:
    for line in file:
        # convert line into list of integers
        numbers = list(map(int, line.split()))
        if safe(numbers) or can_be_safe(numbers):
            safe_report += 1

print(safe_report)
