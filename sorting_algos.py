def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
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

    return swaps

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

if __name__ == "__main__":
    arr = [29, 10, 14, 37, 13, 5, 22]
    swaps = bubble_sort(arr)

    print("Sorted array:")
    for value in arr:
        print(value, end=" ")

    print(f"\nSwaps: {swaps}")