#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def bubble_sort(sequence):
    for i in range(len(sequence) - 1):# just consider the worst case
        for j in range(len(sequence) - (i + 1)):
            if sequence[j + 1] < sequence[j]:# swap position
                tmp = sequence[j + 1]
                sequence[j + 1] = sequence[j]
                sequence[j] = tmp
    return sequence

if __name__ == '__main__':#code above can be called ,and code under this sentence is private
    sequence = np.random.randint(0,20, size = [50])
    print(sequence)
    
    sorted_sequence = bubble_sort(sequence)
    print(sorted_sequence)
