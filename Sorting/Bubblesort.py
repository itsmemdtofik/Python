class BubbleSortOptimization:
    def _f_OptimizedBubbleSort(self, arr):
        for i in range(len(arr) - 1):
            # The variable swapped is a boolean flag that tracks whether 
            # any elements were swapped during a pass of the inner loop.
            # If no swaps were made during a pass, it means that the array is already sorted,
            # and there is no need to continue iterating through the list.
            swapped = False
            for j in range(len(arr) - i - 1):
                # Note down that here we are using the > symbole to ascending order.
                # But if you want this in a descending order then you can chnage this > to <.
                # If you go for selection sort then you will get ulta I mean > symbole for dscending and < for ascending order.
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            if not swapped:
                break
        return arr

def main():
    count = 0
    print("Enter the size of item : ")
    n = int(input())
    print("Enter the number of items : ")
    names = []
    for i in range(n):
        names.append(input())
    
    print("Printing before sorting : ")
    for name in names:
        print(name)
    
    print("Enter the name to be search : ")
    item_string = input()
    for i in range(len(names)):
        if names[i] == item_string:
            count += 1
            break
    
    if count > 0:
        print(f"Item is found : {item_string}\tAt location : {i}\tAnd count is : {count}")
    else:
        print("Item is not present in list !")
    
    for i in range(len(names) - 1):
        for j in range(len(names) - i - 1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
    
    print("Printing after sorting : ")
    for name in names:
        print(name)
    
    # Accessing the array
    new_arr = [-2, 45, 0, 11, -9]
    bbl_sort = BubbleSortOptimization()
    sorted_arr = bbl_sort._f_OptimizedBubbleSort(new_arr)
    
    print("Sorted array are: ")
    for num in sorted_arr:
        print(num)

if __name__ == "__main__":
    main()