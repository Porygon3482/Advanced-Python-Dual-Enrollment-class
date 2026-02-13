# 3.4.py
"""
Name: Neel Srivastava
Assignment: Exercise 3.4: Comparing performances of different sorting algorithm
Date: 11/2/26
Summary:
This file compares the performance of different sorting algorithms for the
same list of integers
"""
import random
import time

start = time.time()


numbers = [random.randint(-200000, 200000) for _ in range(10000)]


#Using Quick Sort
# quick_sort() and partition()

"""
Calls partition to quick sort in 2 seperate sections

:param arr: the list as a parameter
:param low: starting index
:param high: ending index

"""
def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
"""
Picks a pivot and sorts everything being higher/lower than the pivot.
Calls until the list is sorted.

:param arr: the list as a parameter
:param low: starting index
:param high: ending index

:return: the final index of pivot
"""
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

#Bubble sort algorithm
"""
Uses bubble sort to make the list sorted 
:param arr: the list as a parameter
"""
def bubbleSort(arr):
    n = len(arr)

    for k in range(n - 1):
        swapped = False

        for i in range(n - 1 - k):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

    return arr

# Insertion Sort
"""
Using insertion sort to make the list sorted

:param arr: the list as a parameter

"""
def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr

#selection sort
"""
Using selection sort to make the list sorted
:param arr: the list as a parameter
"""
def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minIndex = i

        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr

"""
Sample Output (your times may vary depending on computer speed):

Quick Sort Time: 0.006 seconds
Worst Case Time Complexity: O(n^2)

Bubble Sort Time: 2.16 seconds
Worst Case Time Complexity: O(n^2)

Insertion Sort Time: 0.96 seconds
Worst Case Time Complexity: O(n^2)

Selection Sort Time: 0.87 seconds
Worst Case Time Complexity: O(n^2)
"""


"""
Explanation of Performance Differences:

Quick sort is usually the fastest here because its average-case time complexity
is O(n log n), meaning it divides the list into smaller parts and sorts them
efficiently. However, this implementation can reach O(n^2) in the worst case
because it always chooses the last element as the pivot. If the data is already
sorted or nearly sorted, the partitions become very unbalanced.

Bubble sort, insertion sort, and selection sort are all O(n^2) in the worst case,
so they scale much worse as the list gets large. Bubble sort repeatedly compares
adjacent items and can require many passes. Insertion sort shifts elements and is
often faster than bubble sort, especially if the list is somewhat sorted. Selection
sort always scans the remaining unsorted elements to find the minimum, so it does
about the same number of comparisons no matter what the input looks like.
"""



def main():
    original = numbers  # original random list

    # Quick Sort
    arr = original.copy()
    start = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    print("Quick Sort Time:", end - start, "seconds")
    print("Worst Case Time Complexity: O(n^2)")
    print()

    # Bubble Sort
    arr = original.copy()
    start = time.time()
    bubbleSort(arr)
    end = time.time()
    print("Bubble Sort Time:", end - start, "seconds")
    print("Worst Case Time Complexity: O(n^2)")
    print()

    # Insertion Sort
    arr = original.copy()
    start = time.time()
    insertionSort(arr)
    end = time.time()
    print("Insertion Sort Time:", end - start, "seconds")
    print("Worst Case Time Complexity: O(n^2)")
    print()

    # Selection Sort
    arr = original.copy()
    start = time.time()
    selectionSort(arr)
    end = time.time()
    print("Selection Sort Time:", end - start, "seconds")
    print("Worst Case Time Complexity: O(n^2)")


if __name__ == '__main__':
    main()


