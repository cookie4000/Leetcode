
def twoSum(nums, target):
    for i, a in enumerate(nums, start=0):
        for j, b in enumerate(nums[i+1:], start=0):
            if a+b==target:
                return [i, j+i+1]

# Set input and Target
array = [1, 4, 5, 8, 11]
target = 13

# Print Answer
print(twoSum(array, target))


