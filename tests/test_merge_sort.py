import time
import random
from algorithms.merge_sort import merge_sort


def test_merge_sort():
    """Test function for Merge Sort algorithm."""
    # Test case 1: Test sorting with a small list
    arr1 = [3, 2, 1]
    merge_sort(arr1)
    assert arr1 == [1, 2, 3], "Merge Sort failed for test case 1"

    # Test case 2: Test sorting with a larger list
    arr2 = [5, 8, 1, 3, 9]
    merge_sort(arr2)
    assert arr2 == [1, 3, 5, 8, 9], "Merge Sort failed for test case 2"

    # Performance test: Test sorting with a large list
    arr3 = [random.randint(1, 1000) for _ in range(10000)]
    start_time = time.time()
    merge_sort(arr3)
    end_time = time.time()
    print(f"Merge Sort took {end_time - start_time} seconds for 10000 elements")
