def insertion_sort_descending(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are smaller than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [20, 1, 13, 15, 6]
print("Original array:", arr)

insertion_sort_descending(arr)
print("Sorted array in descending order:", arr)