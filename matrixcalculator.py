# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:04:25 2018

@author: 17Fry
"""
#matrix class
from fractions import Fraction

class Matrix:
    def __init__(self, A = None, b = None):
        #basic qualities of the matrix
        #let A be a list of lists. This is the matrix
        #let b be the solution if it is given
        self.A = A
        self.b = None
        if b and len(b) == len(self.A):
            self.b = b 
        self.RREF = False
        self.transpose = None
        
        #IMT properties
        self.square = False
        self.inv = None
        self.det = None
        #set the inverse to be the identity matrix at first
        if len(self.A) == len(self.A[0]):
            self.inv = [[1 if j == i else 0 for j in range(len(self))] for i in range(len(self))]
            #the determinant
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
        if 0 <= first < len(self) and \
           0 <= second < len(self):
            self.A[first], self.A[second] = self.A[second], self.A[first]
            if self.square:
                self.inv[first], self.inv[second] = self.inv[second], self.inv[first]
                self.det *= -1
            if self.b:
                self.b[first], self.b[second] = self.b[second], self.b[first]           
    
    #scale 1 row by constant c
    def scale(self, row, c):
        if 0 <= row < len(self.A):
            self.A[row] = [c*i if i != 0 else 0.0 for i in self.A[row]]
            if self.square:
                self.inv[row] = [c*i if i != 0 else 0.0 for i in self.inv[row]] 
                self.det *= 1/c       
            if self.b:
                self.b[row] *= c             
        
    #c is a constant that will scale the first row before it's added
    #second will be added to
    def addtwo(self, first, second, c=1):
        if 0 <= first < len(self.A) and \
           0 <= second < len(self.A):
            temp = [c*i for i in self.A[first]]
            self.A[second] = list(map(lambda a,b: a + b, temp, self.A[second]))
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
        smaller = min(len(self.A[0]), len(self.A))

        for step in range(smaller):
            if verbose:
                detailed += f"Step: {str(step)}\n{str(self)}\n"
            #need a non-zero value in [step][step]
            if self.A[step][step] == 0:
                for y in range(step + 1, len(self)):
                    if self.A[y][step] != 0:
                        self.swap(step, y)
                        break
            
            if self.A[step][step] != 0:
                self.scale(step, 1/self.A[step][step])
                #add rows such that all [step + 1 ... len(A)][step] = 0
                for y in range(step + 1, len(self)):
                    const = -1 * (self.A[y][step]/self.A[step][step])
                    self.addtwo(step, y, const)
                #add rows above [0 ... step - 1][step] = 0
                for y in range(step):
                    if self.A[y][step] != 0:
                        const = -1 * (self.A[y][step]/self.A[step][step])
                        self.addtwo(step, y, const)    

        self.RREF = True 
        if verbose:  
            detailed += f"Step: {str(smaller)}\n{str(self)}\n"
            detailed += "Finished!"
        return detailed

    #return the solution of the system if b is provided
    def solution(self):
        if self.b is not None:
            if not self.RREF:
                self.gaussianelimination()
                
            #if any row is all 0's, the system is inconsistent
            for k in self.A:
                if not any(k):
                    return "The system is inconsitent"
            
            #now return the solution if the system is consistent
            if self.square:
                #return "[ " + ", ".join([str(Fraction(x).limit_denominator()) for x in b]) + ' ]'
                return "\n".join([f"x{i} = {str(Fraction(x).limit_denominator())}" for i, x in enumerate(self.b)])
            else: 
                #if M < N, there are free variables. 
                #One free variable for each extra col 
                first = len(self.A[0]) - len(self.A)            
                sol = "The solution in terms of free variables\n"
                for i,l in enumerate(self):
                    tmp = f"x{i+1} = {str(Fraction(self.b[i]).limit_denominator())} + "
                    tmp += ' + '.join([f"{str(Fraction(-w).limit_denominator())}x{z+first}" for z,w in enumerate(l[first:])])
                    sol += f"{tmp}\n"
                return sol
        return "No solution was provided"
    
    #returns the determinant
    def get_det(self):
        if self.square: 
            if not self.RREF:
                self.gaussianelimination()
            #multiply along the diagonal
            for i in range(len(self)):
                self.det *= self.A[i][i]
            return self.det
        #matrix is not square
        return 
                 
    #retruns the determinant
    def get_inverse(self):
        if self.square:
            k = self.get_det()
            if k != 0 and k is not None:
                for j in range(len(self.inv)):
                    g = "["
                    for k in range(len(self.inv[0])):
                        g += str(Fraction(self.inv[j][k]).limit_denominator())
                        g += ", "
                    g = g[:-2]
                    g += "]"
                    print(g)
                return self.inv
            else: 
                #determinant is zero - the inverse DNE
                return None
        else:
            #matrix isn't square
            return None

    '''
    def transpose(self):
        self.transposed = not self.transposed
        if self.square:
            k = len(self)
            for i in range(k):
                for j in range(i, k):
                    self.A[i][j], self.A[j][i] = self.A[j][i], self.A[i][j]
            print(self)
        else:
            transpose = [[0 for j in range(len(self))] for i in range(len(self.A[0]))]
            for k in range(len(self.A[0])):
                for j in range(len(self)):
                    transpose[k][j] = self.A[j][k]
            self.A = transpose
            self.RREF = False
            print(self)               
    '''
    
    """
    def __add__(self,other):
        if len(self) == len(other) and len(self.A[0]) == len(other.A[0]):
            for k in range(len(other)):
                g = self.dot_operation(self.A[k],other.A[k],lambda x,y: x+y)
                print(g)
                self.A[k] = g
        else:
            print("undefined")
    
    def __mul__(self,other):
        if len(self[0]) == len(other):
            
            
        else:
            print("undefined")
    """       
        
    def __iter__(self):
        for x in self.A:
            yield x
            
    def __str__(self): 
        string_rep = ""
        if self.b is None:
            string_rep = [f"| {' '.join([str(Fraction(x).limit_denominator()) for x in y])} |" for y in self]
            return "\n".join(string_rep)   
        else:
            for i in range(len(self)):
                string_rep += f"| {' '.join([str(Fraction(x).limit_denominator()) for x in self.A[i]])} |"
                string_rep += f" {str(Fraction(self.b[i]).limit_denominator())} |\n"
            return string_rep      
    
    def __len__(self):
        return len(self.A)


#n is bigger than m
m = Matrix([[1,2,3,12,13],[4,3,2,14,15]], [6,7])
print(m.solution())

#m = n
m = Matrix([[3,4,5,6],[7,4,3,2],[12,13,2,6],[5,9,8,7]],[12,13,14,15])
print(m.solution())