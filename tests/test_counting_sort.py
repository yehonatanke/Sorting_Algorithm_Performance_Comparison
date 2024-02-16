import time
import random
from algorithms.counting_sort import counting_sort


def test_counting_sort():
    """Test function for Counting Sort algorithm."""
    # Test case 1: Test sorting with a small list
    arr1 = [3, 2, 1]
    sorted_arr1 = counting_sort(arr1)
    assert sorted

    # Test case 2: Test sorting with a larger list
    arr2 = [5, 8, 1, 3, 9]
    sorted_arr2 = counting_sort(arr2)
    assert sorted_arr2 == [1, 3, 5, 8, 9], "Counting Sort failed for test case 2"

    # Performance test: Test sorting with a large list
    arr3 = [random.randint(1, 1000) for _ in range(10000)]
    start_time = time.time()
    counting_sort(arr3)
    end_time = time.time()
    print(f"Counting Sort took {end_time - start_time} seconds for 10000 elements")
