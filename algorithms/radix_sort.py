def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Sorts the given list using Radix Sort.

    Time Complexity:
        - Best Case: O(nk)
        - Average Case: O(nk)
        - Worst Case: O(nk)
    Space Complexity: O(n+k)

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    None: The list is sorted in-place.
    """
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
