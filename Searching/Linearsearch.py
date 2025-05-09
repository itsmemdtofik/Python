
#!Linear Search

def linearSearch():
    """
    Performs linear search on a user-provided array.
    Linear search checks each element sequentially until a match is found.
    """
    try:
        print("Enter the size of elements: ", end='')
        n = int(input())
        
        print("Enter the elements: ")
        arr = []
        for _ in range(n):
            arr.append(int(input()))
        
        print("\nElements are: ")
        for num in arr:
            print(num)
        
        print("\n\nEnter the element to be searched: ", end='')
        item_search = int(input())
        
        count = 0
        position = -1  # -1 indicates not found
        
        for i in range(len(arr)):
            if arr[i] == item_search:
                count += 1
                position = i
                break
        
        if count > 0:
            print(f"The item exists: {item_search}\tAt location: {position}\tCount is {count}")
        else:
            print("Item is not present in array")
        
    except ValueError:
        print("Please enter valid integers!")
    
    print("\n\n")

if __name__ == "__main__":
    """
    Note about Linear Search:
    - Works on both sorted and unsorted arrays
    - Time complexity is O(n) in worst case
    - Simple to implement but inefficient for large datasets
    - Consider binary search (O(log n)) if array is sorted
    """
    linearSearch()