def insertion_sort():
    print("Enter the size of Item : ")
    n = int(input())
    a = []
    print("Enter the number of Items : ")
    for i in range(n):
        a.append(int(input()))
    
    print("Before sorting : ")
    for num in a:
        print(num)
    
    for i in range(1, n):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = temp
    
    print("After sorting : ")
    for num in a:
        print(num)

if __name__ == "__main__":
    insertion_sort()