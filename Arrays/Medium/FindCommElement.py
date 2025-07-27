def findCommonElement(nums1: list, nums2: list, nums3: list):
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set()

    for num in nums3:
        if num in set1 and num in set2 and num not in set3:
            print(num, end=" ")
            set3.add(num)


if __name__ == "__main__":
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    findCommonElement(arr1, arr2, arr3)
