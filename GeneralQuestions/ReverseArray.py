def getReverseArray(nums: list[int]) -> None:
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


arr: list[int] = [1, 0, 3, 4, 5]

getReverseArray(arr)

for i in arr:
    print(i)
