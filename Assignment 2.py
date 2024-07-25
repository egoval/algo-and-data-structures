def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        print(f'Splitting: {A}')
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

        print(f'Merging: {A}')

    return A


product_ids = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
sorted_product_ids = merge_sort(product_ids)
print(f'Sorted array: {sorted_product_ids}')
