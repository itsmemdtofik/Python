"""
 * !Adding one the number represented as a carry of digits.
 *
 * !Approach:
 * Step1: Start from the least significant bit digit(i.g., The last element of an array) and add 1.
 * Step2: If adding 1 to the last element become 10 then set that position to 0
 * and propagate carry. Move this carry 1 to the left element.
 * Step3: If there is no carry, the process stop.
 * Step4: If you reach the most significant digit(the first element) and still have carry, you prepend 1 to array.
 *
 * Example:
 * Input = [1, 2, 4]
 * Output = {1, 2, 5}
 *
 * Input = [9, 9, 9]
 * Output = [1, 0, 0, 0]

"""




def AddOneUsingList(nums):
    if not nums:
        return nums

    result = []
    caryy = 1
    i = len(nums) - 1

    while i >= 0 or caryy > 0:
        digit = nums[i] + caryy if i >= 0 else caryy
        result.insert(0, digit % 10)
        caryy = digit // 10
        i -= 1
    return result


print(f"Using the list:")
print(AddOneUsingList([1, 2, 3]))
print(AddOneUsingList([9, 9, 9]))
print(AddOneUsingList([]))
