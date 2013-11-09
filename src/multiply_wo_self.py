#!/usr/bin/env python

def multiply_wo_self(numbers):
    l = len(numbers)
    output1 = [1] * l
    output2 = [1] * l

    
    i = 1
    while i < l:
        output1[i] = output1[i-1] * numbers[i -1 ]
        i += 1
         
         
    j = l - 2
    
    while j >= 0 :
        output2[j] = output2[j + 1] * numbers[j + 1]
        j -= 1
        
    k = 0
    while k < l:
        output1[k] = output1[k] * output2[k]
        k += 1
        
        
    return output1
        
        
if __name__ == '__main__':
    
    """ [2, 3, 4, 5, 6]
    expected[3*4*5*6, 2*4*5*6, 2*3*5*6, 2*3*4*5]
    """
    

    print multiply_wo_self([2, 3, 4, 5, 6])