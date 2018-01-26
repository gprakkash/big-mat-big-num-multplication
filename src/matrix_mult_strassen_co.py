import math
import os
import random
import time
import statistics
import karatsuba
import numpy as np

timeadd = 0
jointime = 0
dividetime = 0
totaltime = 0
karat = 1

#Format the output for display
def order_matrix(val, row, col, n):
    optarray = []
    strVal = ''
    matrix = np.zeros((n,n));
    for i in range(len(val)):
        matrix[row[i] - 1, col[i] - 1] = val[i]
    for i in range(n):
        for j in range(n):
            strVal = strVal + "{0:0.2f}".format(matrix[i][j]) + "\t"
        optarray.insert(len(optarray), strVal)
        strVal = ''
    finalStr = '\n'.join(optarray)
    print(finalStr)

#Parse the input into Coordinate formate representation
def parseInput(path1,path2):
    size = 0
    global timeadd,jointime, dividetime,totaltime
    file1 = open(path1,'r')
    lineArray1 = file1.readlines()
    file2 = open(path2, 'r')
    lineArray2 = file2.readlines()
    aAA = []
    aJR = []
    aJC = []

    bAA = []
    bJR = []
    bJC = []

    for idx,lines in enumerate(lineArray1):
        if idx == 0:
            size = int(lines)
        else:
            x = int(lines.strip().split(",")[0].replace('(',"",1))
            y = int(lines.strip().split(",")[1])
            z = int(lines.strip().split(",")[2].replace(')',"",1))
            aAA.insert(len(aAA),z)
            aJC.insert(len(aJC),y)
            aJR.insert(len(aJR),x)

    for idx, lines in enumerate(lineArray2):
        if idx == 0:
            size = int(lines)
        else:
            x = int(lines.strip().split(",")[0].replace('(', "", 1))
            y = int(lines.strip().split(",")[1])
            z = int(lines.strip().split(",")[2].replace(')', "", 1))
            bAA.insert(len(bAA), z)
            bJC.insert(len(bJC), y)
            bJR.insert(len(bJR), x)

    # start = time.clock()
    start = time.clock()
    result = MMult([aAA,aJR,aJC],[bAA,bJR,bJC],size)
    print("total time: " + str(time.clock() - start))
    print("add func: " + str(timeadd))
    print("join func: " + str(jointime))
    print("divide func: " + str(dividetime))
    order_matrix(result[0],result[1],result[2],size)
    xxx = 10
    # add([aAA,aJR,aJC],[bAA,bJR,bJC])

# Generate a matrix from coordinate format representation
def generate_matrix(val, row, col, n):
    matrix = np.zeros((n,n));
    for i in range(len(val)):
        matrix[row[i] - 1, col[i] - 1] = val[i]
    return matrix

#Generate Adjacency list
def generate_adj_list(result):
    r_lst = [[],[],[]]
    n = result.shape[0]
    for i in range(n):
        for j in range(n):
            if result[i,j] != 0:
                r_lst[0].append(result[i,j])
                r_lst[1].append(i + 1)
                r_lst[2].append(j + 1)
    return r_lst

#Algorithm Implementation Strassen
def MMult(A,B,n):
    if karat == 1:
        if n == 1:
            return mul(A,B)
    else:
        if n == 4:
            m1 = generate_matrix(A[0], A[1], A[2], n)
            m2 = generate_matrix(B[0], B[1], B[2], n)
            result = np.dot(m1, m2)
            return generate_adj_list(result)
    m = int(n/2)
    x = divideMatrix(A, m)
    y = divideMatrix(B, m)
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    e = y[0]
    f = y[1]
    g = y[2]
    h = y[3]

    p1 = MMult(add(a,d,'add'),add(e,h,'add'),m)
    p2 = MMult(add(c,d,'add'),e,m)
    p3 = MMult(a,add(f,h,'sub'),m)
    p4 = MMult(d,add(g,e,'sub'),m)
    p5 = MMult(add(a,b,'add'),h,m)
    p6 = MMult(add(c,a,'sub'),add(e,f,'add'),m)
    p7 = MMult(add(b,d,'sub'),add(g,h,'add'),m)

    c11 = add(add(p1,p4,'add'),add(p7,p5,'sub'),'add')
    c12 = add(p3,p5,'add')
    c21 = add(p2,p4,'add')
    c22 = add(add(p1,p2,'sub'),add(p3,p6,'add'),'add')

    return join(c11,c12,c21,c22,m)

#Function to add or subtract two matrix
def add(A,B,type):
    global timeadd
    start = time.clock()
    if A[0] == [] and type == 'sub':
        ZZ = [-x for x in B[0]]
        return [ZZ,B[1],B[2]]
    elif B[0] == []:
        return A
    elif A[0] == [] and B[0] == []:
        return [[],[],[]]

    AA = list(A[0])
    aJR = list(A[1])
    aJC = list(A[2])
    BB = list(B[0])
    bJR = list(B[1])
    bJC = list(B[2])
    if type == 'sub':
        BB = [-x for x in BB]
    i = 0
    j = 0
    k = 0
    l = 0
    match = 0
    while i < len(AA):
        while j < len(BB):
            if aJR[i] == bJR[j] and aJC[i] == bJC[j]:
                if karat == 0:
                    AA[i] = AA[i] + BB[j]
                elif karat == 1:
                    AA[i] = addbitwise(AA[i], BB[j])
                BB.pop(j)
                bJR.pop(j)
                bJC.pop(j)
                j = 0
                break
            j = j + 1
        i = i + 1
        j = 0
    AA = AA + BB
    aJR = aJR + bJR
    aJC = aJC + bJC
    timeadd = timeadd + (time.clock() - start)
    return [AA,aJR,aJC]

#Function to add two numbers (bitwise addition)
def addbitwise(a, b):
    global timeadd,countadd
    # start = time.clock()

    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            d = a ^ b ^ (g << 1)
            break
        if ((p | g) << 2) >> i == ~0:
            d = a ^ b ^ ((p | g) << 1)
            break
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1

    return d

#Join four submatrix to form a single matrix - step 4 of strassen multiplication
def join(a,b,c,d,m):
    global jointime
    start = time.clock()
    AA = []
    JR = []
    JC = []
    aAA = list(a[0])
    aJC = list(a[2])
    bAA = list(b[0])
    bJR = list(b[1])
    aJR = list(a[1])
    bJC = list(b[2])
    cAA = list(c[0])
    cJR = list(c[1])
    cJC = list(c[2])
    dAA = list(d[0])
    dJR = list(d[1])
    dJC = list(d[2])
    for idx,x in enumerate(aAA):
        AA.insert(len(AA), aAA[idx])
        JR.insert(len(JR), aJR[idx])
        JC.insert(len(JC), aJC[idx])

    for idx, x in enumerate(bAA):
        AA.insert(len(AA), bAA[idx])
        JR.insert(len(JR), bJR[idx])
        JC.insert(len(JC), bJC[idx] + m)

    for idx, x in enumerate(cAA):
        AA.insert(len(AA), cAA[idx])
        JR.insert(len(JR), cJR[idx] + m)
        JC.insert(len(JC), cJC[idx])

    for idx, x in enumerate(dAA):
        AA.insert(len(AA), dAA[idx])
        JR.insert(len(JR), dJR[idx] + m)
        JC.insert(len(JC), dJC[idx] + m)
    jointime = jointime + (time.clock() - start)
    return [AA,JR,JC]

# Multiplying two base case matrix
def mul(A,B):
    AA = []
    JR = []
    JC = []
    if A[0] == [] or B[0] == []:
        AA.insert(len(AA),0)
    else:
        if A[0][0] > 0 and B[0][0] > 0:
            AA.insert(len(AA),karatsuba.driver_karat([A[0][0]],[B[0][0]]))
        else:
            AA.insert(len(AA), A[0][0] * B[0][0])
    JR.insert(len(JR),1)
    JC.insert(len(JC),1)
    return [AA,JR,JC]

#Divide the matrix into four submatrix
def divideMatrix(A,m):
    global dividetime
    start = time.clock()
    AA1 = list(A[0])
    JR1 = list(A[1])
    JC1 = list(A[2])
    aAA, bAA, cAA, dAA = ([] for i in range(4))
    aJR, bJR, cJR, dJR = ([] for i in range(4))
    aJC, bJC, cJC, dJC = ([] for i in range(4))
    elea, eleb, elec, eled = (0 for i in range(4))

    for idx, x in enumerate(AA1):
        if JC1[idx] <= m and JR1[idx] <= m:
            aAA.insert(len(aAA), x)
            aJC.insert(len(aJC), JC1[idx])
            aJR.insert(len(aJR), JR1[idx])

        if JC1[idx] <= m and JR1[idx] > m:
            cAA.insert(len(cAA), x)
            cJC.insert(len(cJC), JC1[idx])
            cJR.insert(len(cJR), JR1[idx] - m)

        if JC1[idx] > m and JR1[idx] <= m:
            bAA.insert(len(bAA), x)
            bJC.insert(len(bJC), JC1[idx] - m)
            bJR.insert(len(bJR), JR1[idx])

        if JC1[idx] > m and JR1[idx] > m:
            dAA.insert(len(dAA), x)
            dJC.insert(len(dJC), JC1[idx] - m)
            dJR.insert(len(dJR), JR1[idx] - m)
    dividetime = dividetime + (time.clock() - start)
    return [[aAA,aJR,aJC],[bAA,bJR,bJC],[cAA,cJR,cJC],[dAA,dJR,dJC]]


def writeToFile(final):
    toFile = open('output.txt', 'w+')
    toFile.write(final)

parseInput("C:\\Projects\\5311Project\\input_str1.txt","C:\\Projects\\5311Project\\input_str2.txt")