"""
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
 * Step1: Create a temporary array and fill it by 1. We can do it by
 * Arrays.fill(result, 1). [1, 1, 1, 1]. We wil update this one by one.
 * Step2: Use two loop from 0 to n and compute the product.
 * 
 * Arr[] = {1, 2, 3, 4}
 * 
 * result[0] = 24
 * result[1] = 12
 * result[2] = 8
 * result[3] = 6
"""


# This method using division operator
def product_except_self(nums):
    total = 1

    for item in nums:
        total *= item

    print(total)

    result = []
    for item in arr:
        result.append(total // item)
    return result


# Function to calculate the product of all elements except the current element
def productExceptSelf(nums):
    n = len(nums)

    # Initialize the result list as 1
    result = [1] * n

    for i in range(n):

        # Compute the product of all except arr[i]
        for j in range(n):
            if i != j:
                result[i] *= arr[j]

    return result


# Function to calculate the product of all elements except the current element
def productExceptSelfII(nums):
    n = len(nums)
    prefixProduct = [1] * n
    suffixProduct = [1] * n
    result = [0] * n

    # Construct the prefProduct array
    for i in range(1, n):
        prefixProduct[i] = nums[i - 1] * prefixProduct[i - 1]

    # Construct the suffix Product array
    for j in range(n - 2, -1, -1):
        suffixProduct[j] = nums[j + 1] * suffixProduct[j + 1]

    # Construct the result array using prefix Product[] and suffix Product[]
    for i in range(n):
        result[i] = prefixProduct[i] * suffixProduct[i]

    return result


if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)
    print(res)

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    res = productExceptSelfII(arr)
    print(" ".join(map(str, res)))
