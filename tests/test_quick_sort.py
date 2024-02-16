import time
import random
from algorithms.quick_sort import quick_sort


def test_quick_sort():
    """Test function for Quick Sort algorithm."""
    # Test case 1: Test sorting with a small list
    arr1 = [3, 2, 1]
    sorted_arr1 = quick_sort(arr1)
    assert sorted_arr1 == [1, 2, 3], "Quick Sort failed for test case 1"

    # Test case 2: Test sorting with a larger list
    arr2 = [5, 8, 1, 3, 9]
    sorted_arr2 = quick_sort(arr2)
    assert sorted_arr2 == [1, 3, 5, 8, 9], "Quick Sort failed for test case 2"

    # Performance test: Test sorting with a large list
    arr3 = [random.randint(1, 1000) for _ in range(10000)]
    start_time = time.time()
    quick_sort(arr3)
    end_time = time.time()
    print(f"Quick Sort took {end_time - start_time} seconds for 10000 elements")
