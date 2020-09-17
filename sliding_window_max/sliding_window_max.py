'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # left = 0
    # right = k
    # output = []
    # while right <= len(nums):
    #     maxNum = nums[left]
    #     for i in range(left, right):
    #         if nums[i] > maxNum:
    #             maxNum = nums[i]
    #     output.append(maxNum)
    #     left += 1
    #     right += 1
    # return output
    left = 0
    right = k
    output = []
    maxNum = left
    while right <= len(nums):
        if maxNum < left or maxNum == 0:
            maxNum = left
            for i in range(left, right):
                if nums[i] > nums[maxNum]:
                    maxNum = i
        elif nums[maxNum] < nums[right - 1]:
            maxNum = right - 1
        output.append(nums[maxNum])
        left += 1
        right += 1
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
