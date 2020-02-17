# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:55:24 2020

@author: JawKnee
"""

#def modExp(b, n, m):
#    #FIXME: IMPLEMENT THIS METHOD
#    x = 1
#    base_remainder = b % m
#    expo = n
#    count = 0
#    #print(n)
#    for i in range(0,n):
#        check = int(expo % 2) #This is to check to see if you have a remainder of 1
#        #print(check)
#        expo = int(expo / 2) #This is to get the binary form of the exponent so we divide by 2 each iteration of the for loop
#        if check == 1:
#            x = (x * base_remainder) % m #This multiples the number to x when it is 1 in check which represents the position in the binary representation of the exponent
#        #print(base_remainder)
#        base_remainder = (base_remainder * base_remainder) % m #This is to match the binary respentation of the exponent so that the if statement matches the position 
#        #print(count)
#        
#        
#    return x



#def gcd(a,b):
#     #FIXME: IMPLEMENT THIS METHOD
#    
#    if(a<b):
#        temp =b; b = a; a = temp
#    remainder = 1
#    while (remainder != 0):
#        remainder = a % b
#        a = b
#        b = remainder
#        if (remainder!=0):
#            previous_remainder = remainder
#    return previous_remainder
def bezoutCoeffs(a, b):
    #FIXME: IMPLEMENT THIS METHOD.
#        if(a<b):
#            temp = a; a = b;b = temp
#        temp_a = a
#        temp_b = b
        first_coefficient = 1 #s0
        initial_second_coefficient = 0 #t0
        remainder = a%b
        if(remainder == 0):
            return first_coefficient,initial_second_coefficient
        initial_div = -int(a/b) #s1
        print(initial_div)
        second_second_coefficient = 1 #t1
        remainder = a % b
        if(remainder==0):
            return initial_div,second_second_coefficient
        while(remainder!=0):
            
            div_ans = int(a/b)
            the_s_coefficient = first_coefficient - (initial_div*div_ans)
            first_coefficient = initial_div
            initial_div = the_s_coefficient
            #print("here")
            the_t_coefficient = initial_second_coefficient - second_second_coefficient*div_ans
            initial_second_coefficient = second_second_coefficient
            second_second_coefficient = the_t_coefficient
            temp = remainder; a = b;b = temp
            remainder = a % b
            
        
        return the_s_coefficient,the_t_coefficient
                
    
    
    