import matplotlib.pyplot as plt
import numpy as np


def plot_scatterplot(algorithms, timings, input_sizes):
    """
    Plot a scatterplot comparing sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    for i in range(len(algorithms)):
        plt.scatter(input_sizes, timings[i], label=algorithms[i])

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_bar_chart(algorithms, timings, input_sizes):
    """
    Plot a bar chart comparing sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    avg_times = [np.mean(times) for times in timings]
    plt.bar(algorithms, avg_times, color='skyblue')
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Average Execution Time of Sorting Algorithms')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()


def plot_area_chart(algorithms, timings, input_sizes):
    """
    Plot an area chart comparing sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    for i in range(len(algorithms)):
        plt.fill_between(input_sizes, timings[i], label=algorithms[i])

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_bubble_chart(algorithms, timings, input_sizes):
    """
    Plot a bubble chart comparing sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    for i in range(len(algorithms)):
        plt.scatter(input_sizes, timings[i], s=50, label=algorithms[i])

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_histogram(algorithms, timings, input_sizes):
    """
    Plot a histogram comparing sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    for i in range(len(algorithms)):
        plt.hist(timings[i], bins=20, alpha=0.5, label=algorithms[i])

    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Sorting Algorithms Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_line_chart(algorithms, timings, input_sizes):
    """
    Plot a line chart comparing sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    for i in range(len(algorithms)):
        plt.plot(input_sizes, timings[i], label=algorithms[i])

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_pie_chart(algorithms, timings, input_sizes):
    """Plot a pie chart comparing sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    avg_times = [np.mean(times) for times in timings]
    plt.pie(avg_times, labels=algorithms, autopct='%1.1f%%', startangle=140)
    plt.title('Sorting Algorithms Comparison')
    plt.axis('equal')
    plt.show()


def plot_comparison(algorithms, timings, input_sizes):
    """
    Plot the comparison of sorting algorithms.

    Parameters:
    algorithms (list): List of algorithm names.
    timings (list of lists): List of execution times for each algorithm.
    input_sizes (list): List of input sizes.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    for i in range(len(algorithms)):
        plt.plot(input_sizes, timings[i], label=algorithms[i])

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()
