def missing_repeating(number):

    if number is None or len(number) < 2:
        return number
    
    seen = set()
    repeating = -1
    for num in number:
        if num in seen:
            repeating = num
        else:
            seen.add(num)


    missing = -1
    for i in range(1, len(number) + 1):
        if i not in seen:
            missing = i
            break
    return [missing, repeating]

arr = [7, 3, 4, 5, 5, 6, 2]
result = missing_repeating(arr)
print(f"missing: {result[0]} Repeating:{result[1]}")

            
