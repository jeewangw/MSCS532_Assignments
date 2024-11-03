# Insertion Sort in Descending Order
def insertion_sort_descending(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1] that are smaller than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage of Insertion Sort
arr = [20, 1, 13, 15, 6]
print("Original array:", arr)

insertion_sort_descending(arr)
print("Insertion Sort in Descending Order:", arr)

# Quick Sort in Ascending Order
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage of Quick Sort
arr = [20, 1, 10, 15, 6]
print("\nOriginal array:", arr)

arr = quick_sort(arr)  # Reassign to the sorted version
print("Quick Sort in Ascending Order:", arr)

# Merge Sort in Ascending Order
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Helper function for Merge Sort
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

# Example usage of Merge Sort
arr = [20, 2, 13, 15, 6]
print("\nOriginal array:", arr)

arr = merge_sort(arr)  # Reassign to the sorted version
print("Merge Sort in Ascending Order:", arr)
