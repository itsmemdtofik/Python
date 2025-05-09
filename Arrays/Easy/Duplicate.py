
#! Finding duplicate in List(array) in Python

def finding_duplicate(arr):
    seen = set()
    dups = set()

    for i in arr:
        if i in seen:
            dups.add(i)
        else:
            seen.add(i)
    return list(dups)

arr = [-100, 2, 4, 4, 5, 2, 6, 7, 1, -100]

print("The duplicates item in array are : ")
print(finding_duplicate(arr))