#!/usr/bin/python
# -*- coding:UTF-8 -*-
import numpy as np

def quick_sort(arr):
	high = []
	low = []
	pivot_list = []

	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		for i in arr:
			if i < pivot:
				low.append(i)
			elif i > pivot:
				high.append(i)
			else:
				pivot_list.append(i)
		high = quick_sort(high)
		low = quick_sort(low)
	return low + pivot_list + high

if __name__=='__main__':
	lst = np.random.randint(0, 20, size = (50)).tolist()
	result = quick_sort(lst)
	print (result)
