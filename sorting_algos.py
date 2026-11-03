def bubble_sort(arr):
    arr = arr.copy()
    swaps = 0
    n = len(arr)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, swaps

def selection_sort(arr):
    arr = arr.copy()
    swaps = 0
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, swaps

def insertion_sort(arr):
    arr = arr.copy()
    shifts = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1

        arr[j + 1] = key

    return arr, shifts

if __name__ == "__main__":
    # insert array values
    arr = []
    bubble_arr, bubble_swaps = bubble_sort(arr)
    selection_arr, selection_swaps = selection_sort(arr)
    insertion_arr, insertion_shifts = insertion_sort(arr)

    print(f"Array = {arr}")

    print(f"\n- Bubble Sort -\nSorted array: {bubble_arr}\nSwap count: {bubble_swaps}")
    print(f"\n- Selection Sort -\nSorted array: {selection_arr}\nSwap count: {selection_swaps}")
    print(f"\n- Insertion Sort -\nSorted array: {insertion_arr}\nShift count: {insertion_shifts}")