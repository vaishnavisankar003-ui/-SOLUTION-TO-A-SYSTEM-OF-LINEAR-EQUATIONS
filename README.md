# -SOLUTION-TO-A-SYSTEM-OF-LINEAR-EQUATIONS
## Aim:
To write a python program to find a solution to a system of linear equations.
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step 1: 
Import the NumPy library.
### Step 2: Read or define the matrix
### Step 3: Using the np.linalg.solve(), we can find the solutions.
### Step 4: Dispaly the solution of linear equation
End the program
## Program:
#Program to find the solution for the given linear equations.
#Developed by: Vaishnavi.S
#RegisterNumber:212225230289
import numpy as np
matrixA= np.array([[5,-3,-10],[2,2,-3],[-3,-1,5]])
B= np.array([-9,4,-1])
result= np.linalg.solve(matrixA,B)
print(result)
## Output:
<img width="657" height="743" alt="Screenshot 2026-02-03 112132" src="https://github.com/user-attachments/assets/a1497926-b6a6-44ef-9ed2-bbb2d8e4a109" />

## Result: 
Thus the solutions for the linear equations are successfully solved using python program

