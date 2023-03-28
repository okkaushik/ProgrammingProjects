def partition(arr, low, high):
	i = low-1
	pivot = arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1] 
	
	print("Array while sorting"); print(arr)
	return (i+1)

def QuickSort(arr, low, high):
	if len(arr) == 1:
		return arr

	if low < high:
		pi = partition(arr, low, high)
		QuickSort(arr, low, pi-1)
		QuickSort(arr, pi+1, high)


def main():
	arr = ['S','O','R','T','I','N','G']
	n = len(arr)
	print("Elements of the array before sorting:"); print(arr)
	QuickSort(arr, 0, n-1)
	print("Elements of the array after sorting:"); print(arr)

if __name__ == '__main__':
	main()
