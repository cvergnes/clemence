class array(list):

	def __init__(self):
		self.heapSize = 0


def maxHeapify(array, i):
	l = left(i)
	r = right(i)
	if l < array.heapSize and array[i] < array[l] :
		largest = l
	else : 
		largest = i
	if r < array.heapSize and array[largest] < array[r] :
		largest = r
	if largest != i :
		temp = array[i]
		array[i] = array[largest]
		array[largest] = temp
		maxHeapify(array, largest)

def left(i):
	return 2*i;

def right(i):
	return 2*i+1;

def heapSort(array):
	buildMaxHeap(array)
	for i in range(len(array)-1, 0, -1):
		temp = array[i]
		array[i] = array[0]
		array[0] = temp
		array.heapSize -= 1
		maxHeapify(array, 0)

def buildMaxHeap(array):
	array.heapSize=len(array)
	for i in range(len(array)/2,-1,-1):
		maxHeapify(array,i)

list=[5, 3, 50, 1, 8, 3, 67, 32, 4, 9, 14]
ar=array()
ar.extend(list)
print ar
heapSort(ar)
print ar