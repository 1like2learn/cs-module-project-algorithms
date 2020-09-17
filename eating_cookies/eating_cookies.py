'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    arr = [0,0,1]
    i = 0
    while i < n:
        arr.append(arr[0] + arr[1] + arr[2])
        arr.pop(0)
        i += 1
    return arr[2]
    # permut = 0
    # if n - 3 > 0:
    #     print("n: ", n, "n-3: ", n - 3, "permut: ", permut)
    #     permut += eating_cookies(n - 3)
    # elif n - 3 == 0:
    #     permut += 1
    # if n - 2 > 0:
    #     permut += eating_cookies(n - 2)
    #     print("n: ", n, "n-2: ", n - 2, "permut: ", permut)
    # elif n - 2 == 0:
    #     permut += 1
    # if n - 1 > 0:
    #     permut += eating_cookies(n - 1)
    #     print("n: ", n, "n-1: ", n - 1, "permut: ", permut)
    # elif n - 1 == 0:
    #     permut += 1
    # return permut

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 1000

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
