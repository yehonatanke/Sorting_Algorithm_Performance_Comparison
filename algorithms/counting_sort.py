def counting_sort(arr):
    """
    Sorts the given list using Counting Sort.

    Time Complexity:
        - Best Case: O(n + k)
        - Average Case: O(n + k)
        - Worst Case: O(n + k)
    Space Complexity: O(n + k)

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])
    return sorted_arr
