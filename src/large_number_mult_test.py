# -*- coding: utf-8 -*-
"""
Created on Tue May  3 04:37:31 2016

@author: mythcard
"""
import random
import large_multi_brute_force

def generate_digit():
    return random.randrange(0,10)

def generate_number(n):
    number = []
    while n > 0:
        number.append(generate_digit())
        n = n - 1
    return number

#number1 = [1,2,3,4]
number1 = generate_number(256)


#number2 = [2,0]
number2 = generate_number(256)


##  File io
#f = open("large_numberin.txt",'r')
#rd = f.readline()
#number1_v1 = rd.strip()
#number1 = [c for c in number1_v1]
#cnt = 0
#for item in number1:
#    number1[cnt] = int(number1[cnt])
#    cnt = cnt + 1
#rd = f.readline()
#number2_v1 = rd.strip()
#_number2 =  [c for c in number2_v1]
#cnt = 0
#for item in number2:
#    number2[cnt] = int(number2[cnt])
#    cnt = cnt + 1
#f.close()

c = large_multi_brute_force.main(number1, number2)