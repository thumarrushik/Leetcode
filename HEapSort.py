def max_heapify(A, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    parent = i
    if left < n and A[left] < A[parent]:
        parent = left
    if right < n and A[right] < A[parent]:
        parent = right
    if parent != i:
        A[i], A[parent] = A[parent], A[i]
        max_heapify(A, n, parent)
    

def heap_sort(A):
    n = len(A)

    for i in range(n//2, -1,-1):
        max_heapify(A, n, i)

    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A,i,0)



A = [9,6,5,0,8,2,1,3]
heap_sort(A)
print(A)
