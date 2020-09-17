'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    i = 1
    while i < len(arr):
        if arr[i] == arr[0]:
            arr.pop(i)
            arr.pop(0)
            i = 1
        else:
            i += 1
    return arr[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    arr2 = [4, 1, 2, 1, 2]
    arr3 = [2, 2, 1]
    print(f"The odd-number-out is {single_number(arr)} for arr")
    print(f"The odd-number-out is {single_number(arr2)} for arr2")
    print(f"The odd-number-out is {single_number(arr3)} for arr3")