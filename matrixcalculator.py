# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:04:25 2018

@author: 17Fry
"""
#matrix class
from fractions import Fraction

def flt2frac(flt):
    try: 
        answer = str(Fraction(flt).limit_denominator())
        return answer
    except Exception as e:
        return None

class Matrix:
    def __init__(self, A, b = None):
        #basic qualities of the matrix
        #let A be a list of lists. This is the matrix
        len0 = len(A[0])
        for i in A:
            if len(i) != len0:
                raise Exception("Invalid matrix entry")
        self.A = A

        #let b be the solution if it is given
        self.b = None
        if b and len(b) == self.rows():
            self.b = b 
        self.RREF = False
        self.trans = None
        
        #IMT properties
        self.square = False
        self.inv = None
        self.det = None
        #set the inverse to be the identity matrix at first
        if self.rows() == self.cols():
            self.inv = [[1 if j == i else 0 for j in range(self.rows())] for i in range(self.rows())]
            self.det = 1
            self.square = True
            
        #eigenvectors, eigenvalues, and the diagonal matrix
        self.eigenvalues = []
        self.eigenvectors = []
        self.diagonal_matrix = []
        self.P = []

        #orthogonal projections
        self.yhat = []
        self.Q = []
        self.R = []
        self.orthonormal = []  

    #matrix operations  
    #first and second are the indices to swap  
    def swap(self, first, second):   
        if 0 <= first < self.rows() and \
           0 <= second < self.rows():
            self[first], self[second] = self[second], self[first]
            if self.square:
                self.inv[first], self.inv[second] = self.inv[second], self.inv[first]
                self.det *= -1
            if self.b:
                self.b[first], self.b[second] = self.b[second], self.b[first]           
    
    #scale 1 row by constant c
    def scale(self, row, c):
        if 0 <= row < self.rows():
            self[row] = [c*i if i != 0 else 0.0 for i in self[row]]
            if self.square:
                self.inv[row] = [c*i if i != 0 else 0.0 for i in self.inv[row]] 
                self.det *= 1/c       
            if self.b:
                self.b[row] *= c             
        
    #c is a constant that will scale the first row before it's added
    #second will be added to
    def addtwo(self, first, second, c=1):
        if 0 <= first < self.rows() and \
           0 <= second < self.rows():
            temp = [c*i for i in self[first]]
            self[second] = list(map(lambda a,b: a + b, temp, self[second]))
            if self.square:
                temp = [c*i for i in self.inv[first]]
                self.inv[second] = list(map(lambda a,b: a + b, temp, self.inv[second]))
            if self.b:
                temp = c * self.b[first]
                self.b[second] += temp
 
    def gaussianelimination(self, verbose=False):        
        if self.RREF:
            return  
        detailed = ""
        smaller = min(self.rows(), self.cols())

        for step in range(smaller):
            if verbose:
                detailed += f"Step: {step}\n{str(self)}\n"
            #need a non-zero value in [step][step]
            if self[step][step] == 0:
                for y in range(step + 1, self.rows()):
                    if self[y][step] != 0:
                        self.swap(step, y)
                        break
            
            if self[step][step] != 0:
                self.scale(step, 1/self[step][step])
                #add rows such that all [step + 1 ... len(A)][step] = 0
                for y in range(step + 1, self.rows()):
                    const = -1 * (self[y][step]/self[step][step])
                    self.addtwo(step, y, const)
                #add rows above [0 ... step - 1][step] = 0
                for y in range(step):
                    if self[y][step] != 0:
                        const = -1 * (self[y][step]/self[step][step])
                        self.addtwo(step, y, const)    

        self.RREF = True 
        if verbose:  
            detailed += f"Step: {str(smaller)}\n{str(self)}\n"
            detailed += "Finished!"
        if self.det:
            #multiply along the diagonal
            for i in range(self.rows()):
                self.det *= self[i][i]
        return detailed  

    #return the solution of the system if b is provided
    #by default, 
    def solution(self, fract=True):
        if self.b is not None:
            if not self.RREF:
                self.gaussianelimination()
                
            #if any row is all 0's, the system is inconsistent
            for k in self:
                if not any(k):
                    return "The system is inconsitent"
            
            conv = lambda x: flt2frac(x) if fract else x
            #now return the solution if the system is consistent
            if self.square:
                return "\n".join([f"x{i+1} = {conv(x)}" for i, x in enumerate(self.b)]) + "\n"
            else: 
                #if M < N, there are free variables. 
                #One free variable for each extra col 
                first = self.cols() - self.rows()            
                sol = "The solution in terms of free variables\n"
                for i,l in enumerate(self):
                    tmp = f"x{i+1} = {conv(self.b[i])} + "
                    tmp += ' + '.join([f"{conv(-w)}x{z+first}" for z,w in enumerate(l[first-1:])])
                    sol += f"{tmp}\n"
                return sol
        return "No solution was provided"
    
    #returns the determinant
    def determinant(self):
        if self.square: 
            if not self.RREF:
                self.gaussianelimination()
            return self.det
        #matrix is not square
        return 
                 
    #returns the inverse
    def inverse(self):
        if self.square:
            determ = self.determinant() #will do GE if not in RREF
            if determ:
                self.inv = Matrix(self.inv)
                return self.inv
        return 

    def transpose(self):
        result = [[0 for j in range(self.rows())] for i in range(self.cols())]
        for i in range(self.cols()):
            for j in range(self.rows()):
                result[i][j] = self[j][i]
        self.trans = Matrix(result) 
        return self.trans            
    
    def __add__(self,other):
        if self.rows() == other.rows() and \
           self.cols() == other.cols():
            result = [list(map(lambda x,y: x+y, row, other[ind])) for ind,row in enumerate(self)]
            return Matrix(result)

    def __sub__(self,other):
        if self.rows() == other.rows() and \
           self.cols() == other.cols():
            result = [list(map(lambda x,y: x-y, row, other[ind])) for ind,row in enumerate(self)]
            return Matrix(result)
    
    def __mul__(self,other):
        if self.rows() == other.cols() and \
           self.cols() == other.rows():
            #resulting matrix is M1 X M2
            result = [[] for j in other.cols()]
            return Matrix(result)
        return

    def __eq__(self, other):
        if self.rows() != other.rows() or \
           self.cols() != other.cols():
            return False

        for i in range(self.rows()):
            for j in range(self.cols()):
                if self[i][j] != other[i][j]:
                    return False
        return True

    def __getitem__(self, value):
        return self.A[value]

    def __setitem__(self, index, value):
        self.A[index] = value

    def rows(self):
        return len(self.A)

    def cols(self):
        return len(self.A[0])

    def __iter__(self):
        for x in self.A:
            yield x
            
    def __str__(self): 
        string_rep = ""
        if self.b is None:
            string_rep = [f"| {' '.join([flt2frac(x) for x in y])} |" for y in self]
            nl = '\n'
            return f"{nl.join(string_rep)}\n"  
        else:
            for i in range(len(self)):
                string_rep += f"| {' '.join([flt2frac(x) for x in self.A[i]])} |"
                string_rep += f" {flt2frac(self.b[i])} |\n"
            return string_rep      
    
    def __len__(self):
        return len(self.A)


#n = m
m1 = Matrix([[3,4,5,6],[7,4,3,2],[12,13,2,6],[5,9,8,7]],[12,13,14,15])
m1b = Matrix([[4,5,6,7],[10,12,13,14],[2,3,7,8],[6,9,6,9]])
t1 = m1.transpose()
#print(t1)
#print(i1)
#print(m1.solution())
print(m1b - m1)


#n > m
m2 = Matrix([[1,2,3,12,13],[4,3,2,14,15]], [6,7])
m2b = Matrix([[5,6,7,8,9],[12,15,16,20,28]])
t2 = m2.transpose()
print(m2 - m2b)
#print(t2)
#print(m2.solution())

#n < m
m3 = Matrix([[1,2,13],[4,3,15],[16,13,17],[20,21,28]], [6,7,5,6])
t3 = m3.transpose()
#print(t3)
#print(m3.solution())

print(m3 + m2)