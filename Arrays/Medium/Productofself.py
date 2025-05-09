
#! Finding product of an array except self element

#This method using division operator
def product_except_self(arr):
    total = 1

    for item in arr:
        total *= item
    
    print(total)

    result = []
    for item in arr:
        result.append(total // item)
    return result


arr = [1, 2, 3, 4]
print(product_except_self(arr))

#There are also some other method to do so
#Calculating prefix array and suffix array and multiply both into result array.

'''
Approach:

#* Prefix Products: Traverse the array from left to right, storing the product of all elements before the current element.
#* Suffix Products: Traverse the array from right to left, storing the product of all elements after the current element.
#* Result Calculation: Multiply the corresponding prefix and suffix products for each element to get the final result.

'''

def product_except_self(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    output = [1] * n

    print("Prefix array ", prefix)

    # Calculate prefix products
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    print(prefix)

    # Calculate suffix products
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    print(suffix)
    # Calculate the output
    for i in range(n):
        output[i] = prefix[i] * suffix[i]

    return output

# Example usage
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]s