def twoSumDict(nums, target):
    # Empty Dictionary Object
    dict = {}

    # Loop through every number
    for i, num in enumerate(nums, start=0):
        current_difference = target - num 

        # If the number we need is in the dictionary return the index positions of the previous value we say
        # and the current one 
        if current_difference in dict:
            return([dict[current_difference],i])
        
        # If we havent seen the number before add it to the dictionary 
        elif num not in dict:
            dict[num] = i


# Set input and Target
array = [1, 4, 5, 8, 11]
target = 13

print(twoSumDict(array,target))