'''
 * * Product of an Array Except Self.
 * 
 * Given an array arr[] of n integers, construct a product array res[] (of the
 * same size) such that res[i] is equal to the product of all the elements of
 * arr[] except arr[i].
 * 
 * Example:
 * 
 * Input: arr[] = [10, 3, 5, 6, 2]
 * Output: [180, 600, 360, 300, 900]
 * 
 * Explanation:
 * For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
 * For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
 * For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
 * For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
 * For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
 * 
 * Input: arr[] = [12, 0]
 * Output: [0, 12]
 * Explanation:
 * 
 * 
 * For i = 0, res[i] = 0.
 * For i = 1, res[i] = 12.
 * 
 * Approach:
 * Step1: Create a temproray array and fill it by 1. We can do it by
 * Arrays.fill(result, 1). [1, 1, 1, 1]. We wil update this one by one.
 * Step2: Use two loop from 0 to n and compute the product.
 * 
 * Arr[] = {1, 2, 3, 4}
 * 
 * result[0] = 24
 * result[1] = 12
 * result[2] = 8
 * result[3] = 6
'''

# Function to calculate the product of all 
# elements except the current element
def productExceptSelf(arr):
    n = len(arr)

    # Initialize the result list as 1
    res = [1] * n

    for i in range(n):
        
        # Compute the product of all except arr[i]
        for j in range(n):
            if i != j:
                res[i] *= arr[j]

    return res

# Function to calculate the product of all
# elements except the current element
def productExceptSelf(arr):
    n = len(arr)
    prefProduct = [1] * n
    suffProduct = [1] * n
    res = [0] * n

    # Construct the prefProduct array
    for i in range(1, n):
        prefProduct[i] = arr[i - 1] * prefProduct[i - 1]

    # Construct the suffProduct array
    for j in range(n - 2, -1, -1):
        suffProduct[j] = arr[j + 1] * suffProduct[j + 1]

    # Construct the result array using
    # prefProduct[] and suffProduct[]
    for i in range(n):
        res[i] = prefProduct[i] * suffProduct[i]

    return res

if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)
    print(res)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    res = productExceptSelf(arr)
    print(" ".join(map(str, res)))