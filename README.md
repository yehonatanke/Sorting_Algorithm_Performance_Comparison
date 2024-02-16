<div align="center">
  <img src="https://img.shields.io/badge/language-Python-%233776AB.svg?logo=python">
  <img src="https://custom-icon-badges.demolab.com/github/license/denvercoder1/custom-icon-badges?logo=law">
</div>


# Sorting Algorithm Performance Comparison

This program compares the performance of various sorting algorithms.

## Description

The program measures the execution time of each sorting algorithm for different input sizes and plots the comparison. It aims to provide insights into the relative performance of different sorting algorithms under varying input conditions.

# Content Table

1. [Algorithms](#algorithms)
    - [Bubble Sort](#bubble-sort)
    - [Selection Sort](#selection-sort)
    - [Insertion Sort](#insertion-sort)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-sort)
    - [Heap Sort](#heap-sort)
    - [Radix Sort](#radix-sort)
    - [Bucket Sort](#bucket-sort)
    - [Counting Sort](#counting-sort)
    - [Shell Sort](#shell-sort)
2. [Files](#files)
3. [Structure](#structure)
4. [License](#license)
5. [Author](#author)


## Algorithms

### Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

- Time Complexity: $O(n^2)$
- Space Complexity: $O(1)$

### Selection Sort

Selection sort is an in-place comparison sorting algorithm. It divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. It repeatedly selects the minimum element from the unsorted sublist and moves it to the end of the sorted sublist.

- Time Complexity: $O(n^2)$
- Space Complexity: $O(1)$

### Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted list one item at a time. It iterates through the input list, removing one element and inserting it into the correct position in the sorted list.

- Time Complexity: $O(n^2)$
- Space Complexity: $O(1)$

### Merge Sort

Merge sort is a divide-and-conquer algorithm that divides the input list into two halves, sorts each half recursively, and then merges the sorted halves.

- Time Complexity: $O(n \log n)$
- Space Complexity: $O(n)$

### Quick Sort

Quick sort is a divide-and-conquer algorithm that selects a "pivot" element from the list and partitions the other elements into two sublists according to whether they are less than or greater than the pivot. It then recursively sorts the sublists.

- Time Complexity: $O(n \log n)$ average case, $O(n^2)$ worst case
- Space Complexity: $O(\log n)$ average case, $O(n)$ worst case

### Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It builds a max heap from the input list and repeatedly extracts the maximum element from the heap and rebuilds the heap until the list is sorted.

- Time Complexity: $O(n \log n)$
- Space Complexity: $O(1)$

### Radix Sort

Radix sort is a non-comparison sorting algorithm that sorts integers by grouping them by individual digits. It sorts the integers digit by digit from the least significant digit to the most significant digit.

- Time Complexity: $O(nk)$
- Space Complexity: $O(n + k)$

### Bucket Sort

Bucket sort is a distribution-sorting algorithm that distributes the elements of the input list into a number of buckets, then sorts each bucket individually, and finally concatenates the sorted buckets to obtain the sorted list.

- Time Complexity: $O(n + k)$
- Space Complexity: $O(n)$

### Counting Sort

Counting sort is an integer sorting algorithm that operates by counting the number of occurrences of each unique element in the input list and using arithmetic to calculate the position of each element in the output list.

- Time Complexity: $O(n + k)$
- Space Complexity: $O(k)$

### Shell Sort

Shell sort is a variation of insertion sort that allows the exchange of items that are far apart. It sorts the elements by moving elements at distant positions towards each other.

- Time Complexity: $O(n \log n)$ - $O(n^2)$
- Space Complexity: $O(1)$

## Files

- `algorithms/`: Directory containing implementation files for various sorting algorithms.
- `plotting_functions.py`: File containing functions for different types of data visualization.
- `main.py`: Main script to compare the performance of sorting algorithms and generate plots.
- `README.md`: This file, providing an overview of the project.

## Structure

```bash
sorting_algorithms/
│
├── algorithms/
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── heap_sort.py
│   ├── radix_sort.py
│   ├── bucket_sort.py
│   ├── counting_sort.py
│   └── shell_sort.py
│
├── tests/
│   ├── test_bubble_sort.py
│   ├── test_selection_sort.py
│   ├── test_insertion_sort.py
│   ├── test_merge_sort.py
│   ├── test_quick_sort.py
│   ├── test_heap_sort.py
│   ├── test_radix_sort.py
│   ├── test_bucket_sort.py
│   ├── test_counting_sort.py
│   └── test_shell_sort.py
│
├── utils/
│   └── plotting.py
│   
│
├── main.py
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/yehonatanke/Sorting_Algorithm_Performance_Comparison/blob/main/LICENSE) file for details.

## Author

[yehonataKe](https://github.com/yehonatanke)