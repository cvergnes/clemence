def insertionSort(listToSort):
	for i in range(1, len(listToSort)):
		key=listToSort[i]
		j=1
		while i-j>=0 and key < listToSort[i-j]:
			k=i-j
			listToSort[k+1]=listToSort[k]
			j+=1	
		listToSort[(i-j)+1] = key

list=[5, 3, 50, 1, 8 ]
insertionSort(list)
print list
print list == [1, 3, 5, 8, 50]
print range(1, 4)