def intersect(arr1, arr2):
	for i in arr1:
		if i in arr2:
			return 1
	for i in arr2:
		if i in arr1:
			return 1
	return 0

with open('input') as f:
    lines = f.readlines()
ans1 = 0
ans2 = 0
import numpy as temp
for i in lines:
	arr=[]
	i = i.strip('\n').split(',')
	for j in i:
		j = j.split('-')
		arr.append(temp.arange(int(j[0]), int(j[1]) + 1))
	if set(arr[0]).issubset(set(arr[1])) or set(arr[1]).issubset(set(arr[0])):
		ans1 += 1
	ans2 += intersect(arr[0], arr[1])
print('part 1:')
print(ans1)
print('part 2:')
print(ans2)