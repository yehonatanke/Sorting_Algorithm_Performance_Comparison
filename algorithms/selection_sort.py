def selection_sort(arr):
    """
    Sorts the given list using Selection Sort.

    Time Complexity:
        - Best Case: O(n^2)
        - Average Case: O(n^2)
        - Worst Case: O(n^2)
    Space Complexity: O(1)

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    None: The list is sorted in-place.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
