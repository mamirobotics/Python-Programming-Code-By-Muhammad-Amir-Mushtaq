import numpy as np
import control as ctrl
A=np.array([[-3,4],[1,0]]) # system matrix
B=np.array([[1],[0]]) # Input matrix
C=np.array([[1,2]]) #Output
D=np.array([[0]]) # direct transmission matrix
# Create state space
ss=ctrl.ss(A,B,C,D)
ss=ctrl.ss2tf(ss)
print ("transfer function:",ss)
