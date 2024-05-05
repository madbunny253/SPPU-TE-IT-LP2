def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    
    print("Select sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    choice = int(input("Enter your choice (1, 2, 3, or 4): "))

    if choice == 1:
        sorted_arr = bubble_sort(arr.copy())
        print("Sorted array (Bubble Sort):", sorted_arr)
    elif choice == 2:
        sorted_arr = selection_sort(arr.copy())
        print("Sorted array (Selection Sort):", sorted_arr)
    elif choice == 3:
        sorted_arr = merge_sort(arr.copy())
        print("Sorted array (Merge Sort):", sorted_arr)
    elif choice == 4:
        sorted_arr = quick_sort(arr.copy(), 0, len(arr)-1)
        print("Sorted array (Quick Sort):", sorted_arr)
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
