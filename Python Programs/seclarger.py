def second_largest_distinct(arr):
    n = len(arr)
    
    if n < 2:
        return -1
    
    # Initialize first and second largest variables
    first = 0
    second = 0
    
    # Traverse the array to find the maximum and second maximum values
    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] != first and arr[i] > second:
            second = arr[i]
    
    # If second was not updated, it means there was no distinct second largest element
    if second == float('-inf'):
        return -1
    else:
        return second

# Example usage:
arr = [1, 5, 2,  5, 3, 2]
result = second_largest_distinct(arr)
print("Second largest distinct element:", result)
