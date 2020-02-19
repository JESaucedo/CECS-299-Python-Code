# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:55:24 2020

@author: JawKnee
"""

def modExp(b, n, m):
    #FIXME: IMPLEMENT THIS METHOD
    x = 1
    base_remainder = b % m
    expo = n
    for i in range(0,n):
        check = int(expo % 2) #This is to check to see if you have a remainder of 1
        expo = int(expo / 2) #This is to get the binary form of the exponent so we divide by 2 each iteration of the for loop
        if check == 1:
            x = (x * base_remainder) % m 
            #This multiples the number to x when it is 1 in check which represents the position in the binary representation of the exponent
        base_remainder = (base_remainder * base_remainder) % m 
        #This is to match the binary respentation of the exponent so that the if statement matches the position     
    return x


def bezoutCoeffs(a, b):
    #FIXME: IMPLEMENT THIS METHOD.
    first_coefficient = 1 #s0
    initial_second_coefficient = 0 #t0
    remainder = a%b
    if(remainder == 0):
        if(a==0):
            
            return initial_second_coefficient,first_coefficient
        return first_coefficient,initial_second_coefficient
        
    initial_div = -int(a/b) #s1
    second_second_coefficient = 1 #t1
    remainder = a % b
    if(remainder==0):
        return initial_div,second_second_coefficient
    while(remainder!=0):
        div_ans = int(a/b)
        the_s_coefficient = first_coefficient - (initial_div*div_ans)
        #first_coefficient is representing S_k-2
        #the product of initial_div*div_ans is S_k-1
        first_coefficient = initial_div
        #this replaces S_k-2 with S_k-1
        initial_div = the_s_coefficient
        #this replaces S_k-1 with S_k
        the_t_coefficient = initial_second_coefficient - second_second_coefficient*div_ans
        #initial_second_coefficient is representing T_k-2
        #the product of second_second_coefficient*div_ans is representing T_k-1
        initial_second_coefficient = second_second_coefficient
        #this is replacing T_k-2 with T_k-1
        second_second_coefficient = the_t_coefficient
        #this is replacing T_k-1 with T_k
        temp = remainder; a = b;b = temp
        #this is changing the quotient and the remainder
        remainder = a % b
        #this gets a new remainder from the new a and b getting modded to check in the while loop
    return the_s_coefficient,the_t_coefficient

def gcd(a,b):
    #FIXME: IMPLEMENT THIS METHOD
    if(a<b):
        temp =b; b = a; a = temp
    remainder = 1
    while (remainder != 0):
        remainder = a % b
        a = b
        b = remainder
    return a
    
    