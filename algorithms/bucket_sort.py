from algorithms.insertion_sort import insertion_sort


def bucket_sort(arr):
    """Sorts the given list using Bucket Sort.

    Time Complexity:
        - Best Case: O(n + k)
        - Average Case: O(n + k)
        - Worst Case: O(n^2)
    Space Complexity: O(n)

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    None: The list is sorted in-place.
    """
    if len(arr) == 0:
        return

    # Determine the range of elements
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    # Initialize empty buckets
    buckets = [[] for _ in range(range_val)]

    # Distribute elements into buckets
    for num in arr:
        index = (num - min_val) * range_val // (max_val - min_val + 1)
        if buckets[index] is None:
            buckets[index] = []
        buckets[index].append(num)

    # Sort individual buckets and remove None values
    for i in range(range_val):
        if buckets[i] is not None:
            buckets[i] = insertion_sort(buckets[i])

    # Concatenate sorted buckets
    k = 0
    for i in range(range_val):
        if buckets[i] is not None:
            for j in range(len(buckets[i])):
                arr[k] = buckets[i][j]
                k += 1
