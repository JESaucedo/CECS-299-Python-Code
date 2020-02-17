# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:39:50 2020

@author: JawKnee
"""

def binaryAdd(a, b): #this is the beginnning of a Python function
    """ This is the function's docstring
    returns the sum of two binary numbers a and b
    INPUT: a,b - string representation of the binary numbers
    OUPUT: string representation of their sum
    """
    a = a.replace(" ", "") #removing all whitespaces in string a
    b = b.replace(" ", "") #FIXME: REMOVE ALL WHITESPACES IN STRING b
    
    
    m = len(a) #number of digits in string a
    n = len(b) #number of digits in string b
    
    if m < n: #if string a is shorter than string b
        num_missing_zeros = n - m
        a = num_missing_zeros*"0" + a #appending 0's to the beginning of string a, to make it the same length as b
    
    if n < m:
        num_missing_zeros = m - n
        b = num_missing_zeros*"0" + b#FIXME: IF STRING b IS SHORTER THAN STRING a, APPEND 0's TO THE BEGINNING OF STRING b TO MAKE LENGTHS EQUAL
     
    
    #FIXME: FINISH THE FUNCTION SO THAT IT RETURNS THE DESIRED OUTPUT 

    print("a =",a)
    print("b =",b)
    temp_result = ''#this is to temporary hold the result
    first_input_number = len(a)
    #print(len(temp_result))
    carry = 0 #carry
    k = 1
    for i in range(0,first_input_number):
        s_temp = (int(a[first_input_number-k]) + int(b[first_input_number-k]) + int(carry))
        carry = int(s_temp / 2)
        temp_result = str((s_temp) % 2) + temp_result
        k+=1
        i+=1
    if(carry==1):
        temp_result = str(carry) + temp_result
    print(temp_result)
    return temp_result
        