# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:34:34 2020

@author: JawKnee
"""

#Problem 1
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
    return the_s_coefficient#,the_t_coefficient

def modinv(a,m):
    """returns the inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: a inverse as an integer
    """
    result = gcd(a,m)
    if (result != 1):
        raise ValueError("The given values are not relatively prime")
    result = bezoutCoeffs(a,m)
    while (result < 0):
        result = result + m
        
    return result

def letters2digits(letters):
    """converts a string of letters A-Z to a string of double digits without spaces in the range 00-25"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digits = ""  #initializing digits string
    letters = "".join(letters.split()) #removing whitespaces in the text

    
    for i in range(0, len(letters)):
        if(letters[i].isalpha()):
            letter = letters[i].upper()  #converting to uppercase
            digit = letter2digit[letter]
            digits += digit     # concatenating to the string of digits
    
    return digits

def digits2letters(digits):
    """converts a string of double digits without spaces in the range 00-25 to a string of letters A-Z"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digit2letter = dict((v,k) for k,v in letter2digit.items())  #creating a dictionary with keys and values exchanged
        
    letters = ""
    start = 0  #initializing starting index of first digit
    for i in range(0, len(digits), 2):
        digit = digits[start : start + 2]  # accessing the double digit
        letters += digit2letter[digit]     # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    
    return letters

#Problem 2
def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
    result = gcd(a,26)
    if(result != 1):
        raise ValueError("The given key is invalid. The gcd(a,26) must be 1")
    encodedNumbers = letters2digits(text)
    print(encodedNumbers)
    encryptedNumber = ""
    start = 0  #initializing starting index of first digit
    for i in range(0, len(encodedNumbers), 2):
        digit = encodedNumbers[start : start + 2]  # accessing the double digit
       
        newEncryptedNumber = str((a*int(digit) + b) % 26) 
        #this is the function of converting the message into an encoded message and had to cast digit as an integer to do arithmetic and then cast as string to concantanate
        if(int(newEncryptedNumber) < 10):
            newEncryptedNumber = "0" + newEncryptedNumber #this is to make sure that it remains double digits so it can be used in the function digits2letters method
        #print(newEncryptedNumber)
        encryptedNumber += str(newEncryptedNumber)
        start += 2
    encryptedMessage = digits2letters(encryptedNumber)
    return encryptedMessage