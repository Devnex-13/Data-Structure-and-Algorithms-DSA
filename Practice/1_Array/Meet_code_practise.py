def secondLargeUniqueNum(arr):
	l = set(arr)
	if len(l)>1:	
		maxItem1 = max(l)
		l.remove(maxItem1)
		maxItem2 = max(l)
		return maxItem2

arr1 = [10,5,20,20,8,15]
print(secondLargeUniqueNum(arr1))

def evenNum(arr):
	newArr = []
	for i in arr:
		if i%2 == 0:
			newArr.append(i)
	return newArr

arr2 = [1,2,3,4,5,6,7,8]
print(evenNum(arr2))