def MergeSort(A):
    if len(A) > 1:
        m = len(A)//2
        B = A[:m]
        C = A[m:]
        MergeSort(B)
        MergeSort(C)
        Merge(A, B, C)

def Merge(A, B, C):
    i = 0; j = 0; k = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1
        k = k + 1

    if i == len(B):
        while j < len(C):
            A[k] = C[j]
            j = j + 1
            k = k + 1
            print("Array while sorting:"); print(A)
    else:
        while i < len(B):
            A[k] = B[i]
            i = i + 1
            k = k + 1
            print("Array while sorting:"); print(A)

def main():
	arr = ['S','O','R','T','I','N','G']
	print("The array before sorting:"); print(arr)
	MergeSort(arr); print("The sorted array is:"); print(arr)

if __name__ == '__main__':
	main()
