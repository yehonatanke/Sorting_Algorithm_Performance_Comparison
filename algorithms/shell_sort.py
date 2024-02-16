def shell_sort(arr):
    """
    Sorts the given list using Shell Sort.

    Time Complexity:
        - Best Case: O(n log n)
        - Average Case: O(n(log n)^2)
        - Worst Case: O(n(log n)^2)
    Space Complexity: O(1)

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    None: The list is sorted in-place.
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
