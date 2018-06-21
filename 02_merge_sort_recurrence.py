#!/usr/bin/python
# -*- coding:UTF-8 -*-

import numpy as np
def merge_sort(lst):
    sequence = lst
    result = []
    if len(sequence) < 2: #thoughtful
        return sequence
    else:
        mid = int(len(sequence)/2)
        former = merge_sort(sequence[:mid])
        latter = merge_sort(sequence[mid:])
        while(len(former) > 0) or (len(latter) > 0):
            if(len(former) > 0 and len(latter) > 0):
                if former[0] > latter[0]:
                    result.append(latter[0])
                    latter.pop(0)#pop(0) means pop the first element in list, pop() means pop the last one
                else:
                    result.append(former[0])
                    former.pop(0)
            elif len(latter) > 0 and len(former) == 0:
                for i in latter:
                    result.append(i)
                    latter.pop(0)
            elif len(former) > 0 and len(latter) == 0:
                for i in former:
                    result.append(i)
                    former.pop(0)
        return result
        
if __name__ == '__main__':
    lst = np.random.randint(0, 20, size = (50)).tolist()
    consequence = merge_sort(lst)
    print(consequence)