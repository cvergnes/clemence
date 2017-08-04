def countingSort(ls, k):
	c=[0]*(k+1)
	for i in ls:
		c[i] += 1;
	for i in range(1, k+1):
		c[i] += c[i-1]

	res=[0]*len(ls)
	for j in range(len(ls)-1, -1, -1):
		res[c[ls[j]]-1] = ls[j]
		c[ls[j]] -= 1
	return res
		


list=[5, 3, 50, 1, 8, 3, 67, 32, 4, 9, 14]
print list
res = countingSort(list, 67)
print res