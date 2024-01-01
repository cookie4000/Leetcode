def threeSum(nums):

    results = []

    # Sort the Array
    sorted_nums = sorted(nums)

    # Loop through the array
    for i in range(0,len(sorted_nums)):

        # Initialise Pointers
        left = i+1 
        right = len(sorted_nums)-1
        
        # Until they meet (we either move left to the right or right to the left)
        while left < right: 
            cur_value = sorted_nums[i]
            left_value = sorted_nums[left]
            right_value = sorted_nums[right]
            sum = cur_value + left_value + right_value

            # We have an answer
            if sum == 0: 
                results.append((cur_value,left_value,right_value))
                left += 1 
            elif sum < 0: 
                # Increase the lower pointer 
                left += 1
            else: 
                right -= 1 

    # De-deuplicate using set method 
    return (list(set(results)))
    
input = [2, -1, 1, 0, 5, -1, -3]
print(threeSum(input))
