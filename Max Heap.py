def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    parent = i
    if left < len(A) and A[left] > A[parent]:
        parent = left
    if right < len(A) and A[right] > A[parent]:
        parent = right
    if parent != i:
        A[i], A[parent] = A[parent], A[i]
        max_heapify(A, parent)
    
    

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)

A = [9,6,5,0,8,2,1,3]
build_max_heap(A)
print(A)
