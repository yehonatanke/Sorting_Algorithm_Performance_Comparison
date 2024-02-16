def bubble_sort(arr):
    """
    Sorts the given list using Bubble Sort.

    Time Complexity:
        - Best Case: O(n)
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
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
