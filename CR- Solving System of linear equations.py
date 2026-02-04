#Program to find the solution for the given linear equations.
#Developed by: Vaishnavi.S
#RegisterNumber:212225230289
import numpy as np
matrixA= np.array([[5,-3,-10],[2,2,-3],[-3,-1,5]])
B= np.array([-9,4,-1])
result= np.linalg.solve(matrixA,B)
print(result)
