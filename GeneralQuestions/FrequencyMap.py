from collections import defaultdict


def getFrequencyMap(nums: list[int]) -> dict:
    freqMap = defaultdict(int)
    for num in nums:
        freqMap[num] = freqMap[num] + 1
    return dict(freqMap)


def getFrequencyMapII(arr: list[int]):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


# 5. Frequency Map
data = [1, 2, 2, 3, 3, 3, 4]
print("\nFrequency Map:")
print(getFrequencyMap(data))  # {1: 1, 2: 2, 3: 3, 4: 1}
