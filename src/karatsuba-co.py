import os
import sys
import math
import random
import time

timesubs = 0
timeadd = 0
countadd = 0
countrec = 0

#generate numbers randomly for multiplication
def generateNos(n):
    number1 = []
    for index in range(n):
        number1.insert(0,random.randint(0,9))

    number2 = []
    for index in range(n):
        number2.insert(0, random.randint(0, 9))

    start = time.clock()
    result = KM(number1, number2)
    print("total time: " + str(time.clock() - start))
    printResult(number1,number2,result)

#driver for karatsuba multiplication
def driver_karat(num1,num2):

    result = KM(num1, num2)
    resu = map(str, result)
    resu = ''.join(resu)
    opt = int(resu)
    return opt

#print the output in proper format
def printResult(num1,num2,res):
    global timeadd,countrec

    a = map(str, num1)
    a = ''.join(a)
    num1 = int(a)
    print("num1", num1)

    b = map(str, num2)
    b = ''.join(b)
    num2 = int(b)
    print("num2", num2)

    resu = map(str, res)
    resu = ''.join(resu)
    opt = int(resu)

    print("{:,}".format(opt).replace(',', ' '))

    print(num1, " * ", num2)
    print(timeadd)
    print(countadd)
    print(countrec)

#Karatsuba multiplication algorithm
def KM(num1,num2):
    #base case - to do
    global countrec
    countrec = countrec + 1
    len_num1 = len(num1)
    len_num2 = len(num2)

    if len_num1 > len_num2:
        for index in range(len_num1 - len_num2):
            num2.insert(0,0)
    elif len_num1 < len_num2:
        for index in range(len_num2 - len_num1):
            num1.insert(0,0)

    if len_num1 <= 10 and len_num2 <= 10:
        return multiply(num1, num2)

    N = len(num1)

    m0 = int((N + 1) / 2)
    m1 = int(N / 2)

    # Split the inputs in half.
    a = num1[0:m0]
    b = num1[m0:N]
    c = num2[0:m0]
    d = num2[m0:N]

    p = KM(a,c)
    s = KM(b,d)

    temp1 = addbitwise(a,b,[0],'add')
    temp2 = addbitwise(c,d,[0],'add')

    len_temp1 = len(temp1)
    len_temp2 = len(temp2)

    if len_temp1 > len_temp2:
        for index in range(len_temp1 - len_temp2):
            temp2.insert(0, 0)
    elif len_temp1 < len_temp2:
        for index in range(len_temp2 - len_temp1):
            temp1.insert(0, 0)

    temp3 = KM(temp1,temp2)
    temp3 = addbitwise(temp3,p,s, 'sub')

    for index in range(0,2 * m1):
        p.insert(len(p), 0)
    for index in range(0,m1):
        temp3.insert(len(temp3), 0)

    return addbitwise(p,temp3,s,'add')

#function to multiply base case
def multiply(x,y):
    a = map(str, x)
    a = ''.join(a)
    num1 = int(a)

    b = map(str, y)
    b = ''.join(b)
    num2 = int(b)

    c = num1 * num2
    z = str(c)
    res = []
    for digit in z:
        res.append(int(digit))
    return res

#addition of two large numbers
def addbitwise(a, b, c, type):
    global timeadd,countadd
    # start = time.clock()

    a = map(str, a)
    a = ''.join(a)
    a = int(a)

    b = map(str, b)
    b = ''.join(b)
    b = int(b)

    c = map(str, c)
    c = ''.join(c)
    c = int(c)

    if type == 'sub':
        b = -1 * b
        c = -1 * c
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            d = a ^ b ^ (g << 1)
            break
        if ((p | g) << 2) >> i == ~0:
            d = a ^ b ^ ((p | g) << 1)
            break
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1

    a = d
    b = c
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            d = a ^ b ^ (g << 1)
            break
        if ((p | g) << 2) >> i == ~0:
            d = a ^ b ^ ((p | g) << 1)
            break
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1

    z = str(d)
    res = []
    for digit in z:
        res.append(int(digit))
    countadd = countadd + 1
    return res


generateNos(4)






