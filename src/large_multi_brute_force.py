# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:52:30 2016

@author: mythcard
"""
import time


def mult(a,b):
    num = a * b
    digit = num % 10
    carry = int(num / 10)
    return digit,carry
    
def add(a,b):
    num = a + b
    digit = num % 10
    carry = int(num / 10)
    return digit,carry    
    
def add_big_numbers(lst1, lst2):
    final_number = []
    if len(lst1) > len(lst2):
        while len(lst1) != len(lst2):
            lst2.append(0)
    if len(lst2) > len(lst1):
        while len(lst1) != len(lst2):
            lst1.append(0)
    len1 = len(lst1)
    cnt = 0
    carry = 0
    digit = 0
    carry1 = 0
#    print("Lst1 and Lst2: ",lst1, lst2)
    while len1 > 0:
        digit, carry1 = add(lst1[cnt],lst2[cnt])
        if carry == 1:
            digit,carry = add(digit,carry)
#        print("Digit and carry second: ",digit,carry1)
        carry = carry1 + carry
        final_number.append(digit)
        len1 = len1 - 1
        cnt = cnt + 1
    if carry > 0:
        final_number.append(carry)
    return final_number    
        
        
def mult_one_digit_with_rest(number1,a, num_zeros):
    digit = 0
    carry = 0
    lst_number = []
    while num_zeros > 0:
        lst_number.append(0)
        num_zeros = num_zeros  - 1
    for num in number1:
        digit, carry1 = mult(num,a)
        add_digit, carry = add(digit, carry)
        carry = carry + carry1
        lst_number.append(add_digit)
    if carry > 0:    
        lst_number.append(carry)
    return lst_number
    
    
    

def main(number1, number2):
    final_number = ''
    num_zeros = 0
    sum_lst = [0]
    time1 = time.time()
    localtime_start = time.asctime( time.localtime(time.time())) 
    print("Program start time: ",localtime_start)
    
    print("First number is: ", number1)
    number1.reverse()
    print("Second number is: ", number2)
    number2.reverse()    

    itr = 0
    for num in number2:
        sum_lst = add_big_numbers(sum_lst,mult_one_digit_with_rest(number1[:],num,num_zeros))
        print("Iteration stage: ",itr + 1)
        itr = itr + 1
        num_zeros = num_zeros + 1
    
    sum_lst.reverse()
    localtime_end = time.asctime( time.localtime(time.time()))
    
    print("Program ends: ",localtime_end)
    time2 = time.time()
    print("Time taken in seconds",time2 - time1)
    print("Final number length is:",len(sum_lst))
    for item in sum_lst:
        final_number = final_number + str(item)
    final_number = int(final_number)    
    print("Final number is:",final_number)
    return final_number, sum_lst



        
     
                