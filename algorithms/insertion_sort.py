def insertion_sort(arr):
    """
    Sorts the given list using Insertion Sort.

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
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
