import time
import random
from algorithms.bubble_sort import bubble_sort


def test_bubble_sort():
    """Test function for Bubble Sort algorithm."""
    # Test case 1: Test sorting with a small list
    arr1 = [3, 2, 1]
    bubble_sort(arr1)
    assert arr1 == [1, 2, 3], "Bubble Sort failed for test case 1"

    # Test case 2: Test sorting with a larger list
    arr2 = [5, 8, 1, 3, 9]
    bubble_sort(arr2)
    assert arr2 == [1, 3, 5, 8, 9], "Bubble Sort failed for test case 2"

    # Performance test: Test sorting with a large list
    arr3 = [random.randint(1, 1000) for _ in range(10000)]
    start_time = time.time()
    bubble_sort(arr3)
    end_time = time.time()
    print(f"Bubble Sort took {end_time - start_time} seconds for 10000 elements")