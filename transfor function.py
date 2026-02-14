import numpy as np
import control as ctrl
num=[1,2,3]
den=[1,3,4]
tf_system=ctrl.tf(num,den)
print("Transfer function:",tf_system)
ss=ctrl.tf2ss(tf_system)
print("state space presentation")
print('Matrix A:' , ss.A)
print('Matrix B:' , ss.B)
print('Matrix C:' , ss.C)
print('Matrix D:' , ss.D)