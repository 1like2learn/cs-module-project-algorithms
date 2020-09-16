'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    i = 1
    j = 0
    while i < len(arr):
        # print("\ni", arr[i])
        # print("j", arr[j])
        # print("arr: ", arr)
        if arr[i] == arr[j]:
            # print("two items are the same")
            arr.pop(i)
            arr.pop(j)
            i = 1
            j = 0
        else:
            # print("iterate i")
            i += 1
    return arr[j]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    arr2 = [4, 1, 2, 1, 2]
    arr3 = [2, 2, 1]
    print(f"The odd-number-out is {single_number(arr)} for arr")
    # print(f"The odd-number-out is {single_number(arr2)} for arr2")
    # print(f"The odd-number-out is {single_number(arr3)} for arr3")