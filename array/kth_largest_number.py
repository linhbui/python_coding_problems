# 5 implementations
# 1. Brute force
# 2. Selection sort kth times
# This would work even better than 3 if n is large and k is small
    def kth_largest(lst, k):
        n = len(lst)
        for start in range(0, k):
            current_max = lst[start]
            max_index = start
            for i in range(start + 1, n):
                if current_max < lst[i]:
                    max_index = i
                    current_max = lst[i]
            lst[start], lst[max_index] = lst[max_index], lst[start]
        return lst[start]    
# 3. Sort and go to k
# Let's use Bentley's quicksort!        
    def quick_sort(lst, start, end):
        if start >= end:
            return
        pivot = lst[start]
        i = start
        j = end + 1
        while True:
            i += 1
            j -= 1
            while i <= j && lst[i] < pivot:
                i += 1
            while lst[j] > pivot:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[start], arr[i-1] = arr[i-1], arr[start]
        quick_sort(lst, start, i-2)
        quick_sort(lst, i, end)

    def kth_largest(lst, k):
        sorted_list = quicksort(lst, 0, len(lst))
        sorted_list[k - 1]

# 4. Use Heap
# 5. Quick select
