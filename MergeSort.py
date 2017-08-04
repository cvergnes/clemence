def mergeSortInPlace(ls,m,q):
	if m == q:
		return

	p=(m+q)/2
	mergeSortInPlace(ls,m,p)
	mergeSortInPlace(ls,p+1,q)
	mergeInPlace(ls,m,p,q)

def mergeSort(ls):
	if len(ls)<2:
		return ls

	print "MergeSort", ls
	p = len(ls)/2
	left = mergeSort(ls[:p])
	right = mergeSort(ls[p:])
	return merge(left,right)

def mergeInPlace(ls,m,p,q):
	if m==q:
		return 
	i=0
	j=0

	while i+j<=q-m:
		if p+1+j>q or ls[m+i]<ls[p+1+j]:
			i+=1
		else:
			temp = ls[p+1+j]
			for k in range(p+1+j,m+i,-1):
				ls[k]=ls[k-1]	
			ls[m+i]=temp
			j+=1

def merge(left, right):
	if len(left) == 0:
		return right
	if len(right) == 0:
		return left

	i=0
	j=0
	result=[]
	while i<len(left) or j<len(right):
		if i<len(left) and (j>=len(right) or left[i]<right[j]):
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	return result

list=[5, 3, 50, 1, 8]
newList = mergeSort(list)
print newList
print newList == [1, 3, 5, 8, 50]