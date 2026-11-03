def bubble_sort(arr):
    arr = arr.copy()
    swaps = 0
    comparisons = 0
    n = len(arr)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            comparisons += 1

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, comparisons, swaps

def selection_sort(arr):
    arr = arr.copy()
    swaps = 0
    comparisons = 0
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            comparisons += 1

            if arr[j] < arr[min_idx]:
                min_idx = j
            
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, comparisons, swaps

def insertion_sort(arr):
    arr = arr.copy()
    shifts = 0
    comparisons = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons, shifts

if __name__ == "__main__":
    arr = []

    bubble_arr, bubble_comparison, bubble_swaps = bubble_sort(arr)
    selection_arr, selection_comparison, selection_swaps = selection_sort(arr)
    insertion_arr, insertion_comparison, insertion_shifts = insertion_sort(arr)

    print(f"Array = {arr}")

    print(f"\n- Bubble Sort -\nSorted array: {bubble_arr}\nComparisons: {bubble_comparison}\nSwap count: {bubble_swaps}")
    print(f"\n- Selection Sort -\nSorted array: {selection_arr}\nComparisons: {selection_comparison}\nSwap count: {selection_swaps}")
    print(f"\n- Insertion Sort -\nSorted array: {insertion_arr}\nComparisons: {insertion_comparison}\nShift count: {insertion_shifts}")