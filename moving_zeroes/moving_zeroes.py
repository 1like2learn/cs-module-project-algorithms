'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    i = 0
    j = 0
    while i < len(arr):
        if arr[i] != 0:
            arr.insert(j, arr.pop(i))
            j += 1
        i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")