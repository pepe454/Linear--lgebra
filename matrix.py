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
        self.A = A
        self.b = None
        if b is not None:
            if len(b) == len(self.A):
                self.b = b
        self.x = None
        self.RREF = False
        
        #IMT properties
        self.square = False
        self.inv = None
        self.det = None
        if len(self.A) == len(self.A[0]):
            self.inv = [[0 for j in range(len(self))] for i in range(len(self))]
            ind = 0
            for k in range(len(self)):
                self.inv[k][ind] = 1
                ind += 1
            #the determinant
            self.det = 1
            self.square = True
            
        #eigenvectors and eigenvalues
        self.eigenvalues = []
        self.eigenvectors = []
        self.diagonal_matrix = []
        self.P = []
        
            
    #matrix operations    
    def swap(self, first, second):
        def swap2(L,x,y):
            temp = L[x]
            L[x] = L[y]
            L[y] = temp
        if 0 <= first < len(self) and 0 <= second < len(self):
            swap2(self.A, first,second)
            if self.square:
                swap2(self.inv, first,second)
        if self.b is not None:
            swap2(self.b, first,second)
        if self.det:
            self.det *= -1
    
    #scale 1 row
    def scale(self, row, c):
        if 0 <= row < len(self.A):
            self.A[row] = [c*i if i != 0 else 0.0 for i in self.A[row]]
            if self.square:
                self.inv[row] = [c*i if i != 0 else 0.0 for i in self.inv[row]]        
        #update right side
        if self.b:
            self.b[row] *= c 
        if self.det:
            self.det *= 1/c
        
    def dot_operation(self,x,y,f=lambda y,k: y):
        for j in range(len(x)):
            y[j] = f(x[j],y[j])
         
    def addtwo(self, first, second, c=1):
        if 0 <= first < len(self.A) and 0 <= second < len(self.A):
            temp = [c*i for i in self.A[first]]
            self.dot_operation(temp,self.A[second],lambda a,b: a + b)
            if self.square:
                temp = [c*i for i in self.inv[first]]
                self.dot_operation(temp,self.inv[second],lambda a,b: a + b)
            if self.b:
                temp = c * self.b[first]
                self.b[second] += temp
 
    def gaussianelimination(self):        
        if self.RREF:
            return  
        step = 0
        while step < len(self.A[0]) and step < len(self):
            print("Step: " + str(step))
            print("Matrix: ")
            print(self)
            if self.A[step][step] == 0:
                for y in range(step + 1, len(self)):
                    if self.A[y][step] != 0:
                        self.swap(step, y)
                        break
            
            if self.A[step][step] != 0:
                self.scale(step, 1/self.A[step][step])
                for y in range(step + 1, len(self)):
                    const = -1 * (self.A[y][step]/self.A[step][step])
                    self.addtwo(step, y, const)
                for y in range(step):
                    if self.A[y][step] != 0:
                        const = -1 * (self.A[y][step]/self.A[step][step])
                        self.addtwo(step, y, const)    
                
            step += 1
            
        if step >= len(self) or step >= len(self.A[0]):
            step -= 1            
        self.RREF = True
        #makes each b a fraction instead of decimal
        if self.b is not None:
            newb = []
            for k in self.b:
                newb.append(Fraction(k).limit_denominator())
            self.b = newb
            
        print("Finished \n" + str(self))

    #return the solution of the system if b is provided
    def solve(self):
        #need to account for free variables and inconsistent solutions        
        if self.b is not None:
            if not self.RREF:
                self.gaussianelimination()
                
            #check to make sure that zero rows match up with zero bi
            count = -1
            for k in self.A:
                count += 1
                zero = True
                for j in k:
                    if j != 0:
                        zero = False
                        break
                if zero:
                    if self.b[count] != 0:
                        return "Inconsitent solution!"
                    
            if len(self) >= len(self.A[0]):
                temp = "["
                for i in self.b: 
                    temp += str(i) + ", "
                temp = temp[:-2]
                temp += "]"
                return temp
            
            #check for inconsitent solution when m > n:
            if len(self) < len(self.A[0]):
                sol = ""
                first = len(self.A[0]) - len(self.A)
                for i in range(len(self)):
                    sol += "x" + str(i) + " = " + str(self.b[i]) + " + " 
                    temp = ""
                    for j in range(first, len(self.A[0])):
                        temp += "({cons})x{place}".format(place=j,cons=str(Fraction(self.A[i][j]).limit_denominator()))
                        if j != len(self.A[0]) - 1:
                            temp += " + "
                    sol += temp + "\n"
                return "The solution in terms of free variables: \n" + sol
                 
    #doesn't return in a satisfying way, but it's something
    def get_inverse(self):
        k = self.get_det()
        if k != 0:
            for yaga in range(len(self.inv)):
                g = "["
                for yeet in range(len(self.inv[0])):
                    g += str(Fraction(self.inv[yaga][yeet]).limit_denominator())
                    if yeet < len(self.inv[0]) - 1:
                        g += ", "
                g += "]"
                print(g)
            return self.inv
        else:
            return "Determinant is zero"
    
    #returns the determinant
    def get_det(self):
        #checking to see if there are any zero rows
        yaga = False
        for i in range(len(self)):
            if self.A[i][0] == 0:
                count = 0
                for j in range(1,len(self.A[0])):
                    count += self.A[i][j]
                if count == 0:
                    yaga = True
                    break
        #in that case, det is zero. If rows!=cols, det is zero or undefined but yaga?
        if yaga or len(self) != len(self.A[0]):
            return 0
        elif not self.RREF:
            self.gaussianelimination()
        ind = 0
        #if there are any zero rows, determinant is zero
        for i in range(len(self)):
            self.det *= self.A[i][ind]
            ind += 1
        return self.det
    
    #need to check this method
    def __add__(self,other):
        if len(self) == len(other) and len(self.A[0]) == len(other.A[0]):
            for k in range(len(other)):
                g = self.dot_operation(self.A[k],other.A[k],lambda x,y: x+y)
                print(g)
                self.A[k] = g
        else:
            print("undefined")
    
    """
    def __mul__(self,other):
        if len(self[0]) == len(other):
            
            
        else:
            print("undefined")
    """        
    
        
    def __iter__(self):
        for x in self.A:
            yield x
            
    def __str__(self): 
        strng = ""
        if self.b is None:
            for y in self:
                strng += str(y) + "\n"
        else:
            i = 0
            for y in self:
                strng += str(y) + " " + str("[" + str(self.b[i]) + "]") + "\n"
                i += 1
        return strng
    
    def __len__(self):
        return len(self.A)


#n is bigger than m
m = Matrix([[1,2,3,12,13],[4,3,2,14,15]],[10,12])
print(m.solve())
print("----------------\n\n")

#m is bigger than m
m = Matrix([[1,2,3],[4,3,2],[6,7,5],[3,8,7],[12,3,14],[13,40,32]],[1,2,3,4,5,6])
print(m.solve())
print("----------------\n\n")

#m = n
m = Matrix([[3,4,5,6],[7,4,3,2],[12,13,2,6],[5,9,8,7]],[12,13,14,15])
print(m.solve())





