# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:38:11 2016

@author: mythcard
"""

"""
matrix in list of list representation
"""

from copy import deepcopy
import random
import time

matrix_a_lstoflst = []
matrix_b_lstoflst = []
list_a1_row = [4,1,0,0]
list_a2_row = [0,4,1,0]
list_a3_row = [0,1,4,0]
list_a4_row = [0,0,1,4]
list_b1_row = [25,3,0,1]
list_b2_row = [0,1,2,0]
list_b3_row = [1,0,0,0]
list_b4_row = [0,1,4,0]

#list_a1_row = [1,2,3,4,5,6,7,8]
#list_a2_row = [5,6,7,8,9,10,11,12]
#list_a3_row = [1,2,3,4,5,6,7,8]
#list_a4_row = [5,6,7,8,9,10,11,12]
#list_a5_row = [1,2,3,4,5,6,7,8]
#list_a6_row = [5,6,7,8,9,10,11,12]
#list_a7_row = [1,2,3,4,5,6,7,8]
#list_a8_row = [5,6,7,8,9,10,11,12]
#list_b1_row = [1,2,3,4,5,6,7,8]
#list_b2_row = [5,6,7,8,9,10,11,12]
#list_b3_row = [1,2,3,4,5,6,7,8]
#list_b4_row = [5,6,7,8,9,10,11,12]
#list_b5_row = [1,2,3,4,5,6,7,8]
#list_b6_row = [5,6,7,8,9,10,11,12]
#list_b7_row = [1,2,3,4,5,6,7,8]
#list_b8_row = [5,6,7,8,9,10,11,12]

matrix_a_lstoflst.append(list_a1_row)
matrix_a_lstoflst.append(list_a2_row)
matrix_a_lstoflst.append(list_a3_row)
matrix_a_lstoflst.append(list_a4_row)
#matrix_a_lstoflst.append(list_a5_row)
#matrix_a_lstoflst.append(list_a6_row)
#matrix_a_lstoflst.append(list_a7_row)
#matrix_a_lstoflst.append(list_a8_row)

matrix_b_lstoflst.append(list_b1_row)
matrix_b_lstoflst.append(list_b2_row)
matrix_b_lstoflst.append(list_b3_row)
matrix_b_lstoflst.append(list_b4_row)
#matrix_b_lstoflst.append(list_b5_row)
#matrix_b_lstoflst.append(list_b6_row)
#matrix_b_lstoflst.append(list_b7_row)
#matrix_b_lstoflst.append(list_b8_row)

## generation of a square matrix
def generate_matrix(matrix_order):
    matrix_c_lstoflst = []
    lst = []
    m = matrix_order
    while m > 0:
        n = matrix_order
        lst =[]
        while n > 0:
            lst.append(random.randrange(0,10))
            n = n - 1
        matrix_c_lstoflst.append(lst)
        m = m -1 
    return matrix_c_lstoflst 
    
def generate_matrix1(matrix_order):
    matrix_c_lstoflst = []
    lst = []
    m = matrix_order
    f = open("matrix_in111.txt",'w')
    f.writelines(str(matrix_order))
    f.writelines('\n')
    row = 0
    col = 0
    while m > 0:
        n = matrix_order
        lst =[]
        while n > 0:
            var = random.randrange(0,10)
            lst.append(var)
            f.writelines('(')
            f.writelines(str(row + 1))
            f.writelines(',')
            f.writelines(str(col + 1))
            f.writelines(',')
            f.writelines(str(var))
            f.writelines(')')
            f.writelines('\n')
            n = n - 1
            col = col + 1
        matrix_c_lstoflst.append(lst)
        m = m -1
        row = row + 1
        col = 0
    f.close()     
    return matrix_c_lstoflst    
    
def generate_matrix2(matrix_order):
    matrix_c_lstoflst = []
    lst = []
    m = matrix_order
    f = open("matrix_in222.txt",'w')
    f.writelines(str(matrix_order))
    f.writelines('\n')
    row = 0
    col = 0
    while m > 0:
        n = matrix_order
        lst =[]
        while n > 0:
            var = random.randrange(0,10)
            lst.append(var)
            f.writelines('(')
            f.writelines(str(row + 1))
            f.writelines(',')
            f.writelines(str(col + 1))
            f.writelines(',')
            f.writelines(str(var))
            f.writelines(')')
            f.writelines('\n')
            n = n - 1
            col = col + 1
        matrix_c_lstoflst.append(lst)
        m = m -1
        row = row + 1
        col = 0
    f.close()     
    return matrix_c_lstoflst    
    
def generate_matrix_sparse1(matrix_order):
    matrix_c_lstoflst = []
    lst = []
    m = matrix_order
    f = open("matrix_in11.txt",'w')
    f.writelines(str(matrix_order))
    f.writelines('\n')
    row = 0
    col = 0
    while m > 0:
        n = matrix_order
        lst =[]
        while n > 0:
            pareto_par = random.paretovariate(1)
            if pareto_par > 5.0:
                var = random.randrange(1,10)
                lst.append(var)
                f.writelines('(')
                f.writelines(str(row + 1))
                f.writelines(',')
                f.writelines(str(col + 1))
                f.writelines(',')
                f.writelines(str(var))
                f.writelines(')')
                f.writelines('\n')
            else:
                lst.append(0)
            n = n - 1
            col = col + 1
        matrix_c_lstoflst.append(lst)
        m = m -1 
        row = row + 1
        col = 0
    f.close()    
    return matrix_c_lstoflst 
    
def generate_matrix_sparse2(matrix_order):
    matrix_c_lstoflst = []
    lst = []
    m = matrix_order
    f = open("matrix_in22.txt",'w')
    f.writelines(str(matrix_order))
    f.writelines('\n')
    row = 0
    col = 0
    while m > 0:
        n = matrix_order
        lst =[]
        while n > 0:
            pareto_par = random.paretovariate(1)
            if pareto_par > 5.0:
                var = random.randrange(1,10)
                lst.append(var)
                f.writelines('(')
                f.writelines(str(row + 1))
                f.writelines(',')
                f.writelines(str(col + 1))
                f.writelines(',')
                f.writelines(str(var))
                f.writelines(')')
                f.writelines('\n')
            else:
                lst.append(0)
            n = n - 1
            col = col + 1
        matrix_c_lstoflst.append(lst)
        m = m -1 
        row = row + 1
        col = 0
    f.close()    
    return matrix_c_lstoflst    

def number_multipy(a, b):
    return a * b
    

def shortest_matrix_multiply(matrix_a_lstoflst , matrix_b_lstoflst):
    matrix_c_lstoflst = []
    list_c1_row = []
    list_c2_row = []
    m1 = (matrix_a_lstoflst[0][0] + matrix_a_lstoflst[1][1]) * (matrix_b_lstoflst[0][0] + matrix_b_lstoflst[1][1])
    m2 = (matrix_a_lstoflst[1][0] + matrix_a_lstoflst[1][1]) * (matrix_b_lstoflst[0][0]) 
    m3 = (matrix_a_lstoflst[0][0] ) * (matrix_b_lstoflst[0][1] - matrix_b_lstoflst[1][1])
    m4 = (matrix_a_lstoflst[1][1] ) * (matrix_b_lstoflst[1][0] - matrix_b_lstoflst[0][0])
    m5 = (matrix_a_lstoflst[0][0] + matrix_a_lstoflst[0][1]) * (matrix_b_lstoflst[1][1])
    m6 = (matrix_a_lstoflst[1][0] - matrix_a_lstoflst[0][0]) * (matrix_b_lstoflst[0][0] + matrix_b_lstoflst[0][1])
    m7 = (matrix_a_lstoflst[0][1] - matrix_a_lstoflst[1][1]) * (matrix_b_lstoflst[1][0] + matrix_b_lstoflst[1][1])
    list_c1_row.append(m1 + m4 - m5 + m7)
    list_c1_row.append(m3 + m5)
    matrix_c_lstoflst.append(list_c1_row)
    list_c2_row.append(m2 + m4)
    list_c2_row.append(m1 - m2 + m3 + m6)
    matrix_c_lstoflst.append(list_c2_row)
    return matrix_c_lstoflst     


### the matrix passes to this definition should always be 2 * 2
def matrix_add(matrix_a_lstoflst,matrix_b_lstoflst, matrix_order):
    matrix_c_lstoflst = []
    list_c1_row = []
    for i in range(0,matrix_order):
        for j in range(0,matrix_order):
            list_c1_row.append(matrix_a_lstoflst[i][j] + matrix_b_lstoflst[i][j])
        matrix_c_lstoflst.append(list_c1_row)
        list_c1_row = []
    return matrix_c_lstoflst

def matrix_sub(matrix_a_lstoflst,matrix_b_lstoflst, matrix_order):
    matrix_c_lstoflst = []
    list_c1_row = []
    for i in range(0,matrix_order):
        for j in range(0,matrix_order):
            list_c1_row.append(matrix_a_lstoflst[i][j] - matrix_b_lstoflst[i][j])
        matrix_c_lstoflst.append(list_c1_row)
        list_c1_row = []
    return matrix_c_lstoflst
    
def create_sub_matrix(matrix, matrix_division_order, code):
    final_matrix = []
    list_row = []
    if code == '11':
        starti = 0
        endi = matrix_division_order
        startj = 0
        endj = matrix_division_order
    elif code == '21':
        starti = matrix_division_order
        endi = 2 * matrix_division_order
        startj = 0
        endj = matrix_division_order
    elif code == '12':
        starti = 0
        endi = matrix_division_order
        startj = matrix_division_order
        endj = 2 * matrix_division_order
    elif code == '22':
        starti = matrix_division_order
        endi = 2 * matrix_division_order
        startj = matrix_division_order
        endj = 2 * matrix_division_order
    for i in range(starti,endi):
        for j in range(startj,endj):
            list_row.append(matrix[i][j])
        final_matrix.append(list_row)
        list_row = []
    return final_matrix   

def matrix_multiply(matrix_a_lstoflst, matrix_b_lstoflst, matrix_order):
     final_matrix = []
     if matrix_order == 2:
         a = deepcopy(matrix_a_lstoflst)
         b = deepcopy(matrix_b_lstoflst)
         return shortest_matrix_multiply(a,b)
     else:
         a = deepcopy(matrix_a_lstoflst)
         b = deepcopy(matrix_b_lstoflst)
         matrix_division_order = int(matrix_order /2)
         a11 = create_sub_matrix(a, matrix_division_order, '11')
         a12 = create_sub_matrix(a, matrix_division_order, '12')
         a21 = create_sub_matrix(a, matrix_division_order, '21')
         a22 = create_sub_matrix(a, matrix_division_order, '22')
         b11 = create_sub_matrix(b, matrix_division_order, '11')
         b12 = create_sub_matrix(b, matrix_division_order, '12')
         b21 = create_sub_matrix(b, matrix_division_order, '21')
         b22 = create_sub_matrix(b, matrix_division_order, '22')
         m1 = matrix_multiply(matrix_add(a11,a22, matrix_division_order) ,matrix_add(b11,b22, matrix_division_order),matrix_division_order)
#         print("Matrix m1: ",m1)
         m2 = matrix_multiply(matrix_add(a21,a22, matrix_division_order) , b11 ,matrix_division_order)
#         print("Matrix m2: ",m2)
         m3 = matrix_multiply(a11, matrix_sub(b12,b22, matrix_division_order) , matrix_division_order)
#         print("Matrix m3: ",m3)
         m4 = matrix_multiply(a22, matrix_sub(b21,b11, matrix_division_order) , matrix_division_order)
#         print("Matrix m4: ",m4)
         m5 = matrix_multiply(matrix_add(a11,a12, matrix_division_order) , b22 ,matrix_division_order)
#         print("Matrix m5: ",m5)
         m6 = matrix_multiply(matrix_sub(a21,a11, matrix_division_order) ,matrix_add(b11,b12, matrix_division_order),matrix_division_order)
#         print("Matrix m6: ",m6)
         m7 = matrix_multiply(matrix_sub(a12,a22, matrix_division_order) ,matrix_add(b21,b22, matrix_division_order),matrix_division_order)
#         print("Matrix m7: ",m7)
         c11 = matrix_add(matrix_sub(matrix_add(m1,m4,matrix_division_order),m5, matrix_division_order),m7,matrix_division_order)
#         print("C11 matrix: ",c11)
         c12 = matrix_add(m3,m5,matrix_division_order)
         c21 = matrix_add(m2,m4,matrix_division_order)
         c22 = matrix_add(matrix_add(matrix_sub(m1,m2,matrix_division_order),m3, matrix_division_order),m6,matrix_division_order)
#         print("C11: ",c11)
#         print("C12: ",c12)
#         print("C21: ",c21)
#         print("C22: ",c22)
         lst = []
         for i in range(0,matrix_division_order):
             for j in range(0,matrix_division_order):
                 lst.append(c11[i][j])
             final_matrix.append(lst)    
             lst = []
         for i in range(0,matrix_division_order):
             for j in range(0,matrix_division_order):
                 lst.append(c12[i][j])
             while len(lst) > 0:    
                 final_matrix[i].append(lst.pop(0))    
             lst = [] 
         for i in range(0,matrix_division_order):
             for j in range(0,matrix_division_order):
                 lst.append(c21[i][j])
             final_matrix.append(lst)    
             lst = []
         for i in range(0,matrix_division_order):
             for j in range(0,matrix_division_order):
                 lst.append(c22[i][j])
             while len(lst) > 0:    
                 final_matrix[i + matrix_division_order].append(lst.pop(0))    
             lst = []    
         return final_matrix
         



### a 2 * 2 matrix addition only
#a = deepcopy(matrix_a_lstoflst)
#b = deepcocpy(matrix_b_lstoflst)
time1 = time.time()
matrix_order =4
localtime_start = time.asctime( time.localtime(time.time())) 
print("Program start time with dimension and start time: ",matrix_order,localtime_start)

a = generate_matrix1(matrix_order)
b = generate_matrix2(matrix_order)

#a = generate_matrix_sparse1(matrix_order)
#b = generate_matrix_sparse2(matrix_order)

c = matrix_multiply(a, b, matrix_order)
localtime_end = time.asctime( time.localtime(time.time()))
print("Program ends: ",localtime_end)
time2 = time.time()
print("Time taken in seconds",time2 - time1)

    


