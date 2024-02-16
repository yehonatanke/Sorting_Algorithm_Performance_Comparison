import time
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from algorithms.radix_sort import radix_sort
from algorithms.bucket_sort import bucket_sort
from algorithms.counting_sort import counting_sort
from algorithms.shell_sort import shell_sort
from utils.plotting import *


def generate_random_list(size):
    """
    Generate a random list of integers.

    Parameters:
    size (int): Size of the list.

    Returns:
    list: Random list of integers.
    """
    return [random.randint(1, 1000) for _ in range(size)]


def measure_time_sort(sort_func, arr):
    """
    Measure the execution time of a sorting function.

    Parameters:
    sort_func (function): Sorting function to be tested.
    arr (list): List to be sorted.

    Returns:
    float: Execution time in seconds.
    """
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time


def compare_sorting_algorithms(input_sizes):
    """Compare the performance of various sorting algorithms.

    Parameters:
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    # Define sorting algorithms
    algorithms = [
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort",
        "Heap Sort",
        "Radix Sort",
        "Bucket Sort",
        "Counting Sort",
        "Shell Sort"
    ]

    # Initialize an empty list to store timings for each algorithm
    timings = [[] for _ in range(len(algorithms))]

    # Measure execution time for each algorithm and input size
    for size in input_sizes:
        arr = generate_random_list(size)
        for i, algorithm in enumerate(algorithms):
            sort_func = globals()[algorithm.lower().replace(" ", "_")]
            time_taken = measure_time_sort(sort_func, arr.copy())
            timings[i].append(time_taken)

    # Plot the comparison of sorting algorithms using different types of plots
    plot_scatterplot(algorithms, timings, input_sizes)
    plot_bar_chart(algorithms, timings, input_sizes)
    plot_area_chart(algorithms, timings, input_sizes)
    plot_bubble_chart(algorithms, timings, input_sizes)
    plot_histogram(algorithms, timings, input_sizes)
    plot_line_chart(algorithms, timings, input_sizes)
    plot_pie_chart(algorithms, timings, input_sizes)
    plot_comparison(algorithms, timings, input_sizes)


if __name__ == "__main__":
    input_sizes = [100, 500, 1000, 2000]
    compare_sorting_algorithms(input_sizes)
