#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import numpy as np

def merge_sort(lst, low, mid, high):# merge part
    former = lst[low:mid]
    latter = lst[mid:high]
    result = []
    while(len(former) > 0) or (len(latter) > 0):
        if(len(former) > 0 and len(latter) > 0):
            if(former[0] < latter[0]):
                result.append(former[0])
                former.pop(0)
            else:
                result.append(latter[0])
                latter.pop(0)
        elif(len(former) > 0 and len(latter) == 0):
            for i in former:
                result.append(i)
                former.pop(0)
        elif(len(latter) > 0 and len(former) == 0):
            for i in latter:
                result.append(i)
                latter.pop(0)
    return result

if __name__ == '__main__':
    lst = np.random.randint(0, 20, size = (50)).tolist()
    i = 1
    consequence = []
    while i < len(lst):# low = low + 2i, mid = low + i, high = low + 2i(in groups)
        low = 0     
        while low < len(lst):
            mid = low + i
            high = min(low + 2 * i, len(lst))
            #if mid < high:
            for j in merge_sort(lst, low, mid, high):
                consequence.append(j)        
            low += 2 * i
        i *= 2
        lst = consequence
        consequence = []
    else:
        print(lst)

