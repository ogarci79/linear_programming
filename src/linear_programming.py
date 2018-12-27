#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import *
from scipy import linalg 

def main():
    print("Main")

    #A=np.array([[1,1,0,0,4.5],[0,0,1,1,6],[1,1,1,1,15]])
    #A=np.array([[4,3,0,0],[-4,-2,10,0],[0.5,0.3,2,0],[-1,0,0,0],[0,-1,0,0]])
    #A=np.array([[2,1,1,-12,-1],[-1,2,3,-9,-1],[3,4,-1,-6,-1],[4,-3,2,0,1]])
    A=np.array([[2,1,1,0,1,0,0,180],[1,3,2,0,0,1,0,300],[2,1,2,0,0,0,1,240],[-6,-5,-4,1,0,0,0,0]])
    M=sp.Matrix(A)
    #print np.dot(A.T,A)
    print M.rref()

if __name__ == "__main__":
    main()

