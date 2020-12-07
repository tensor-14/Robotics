import numpy as np
import math as sp

n = int(input("Enter the number of rows for DH table: "))
values = []
matrices = []
temp = np.identity(4)

for i in range(n):
  theta, aplha, d, a = input("Enter the values of theta, alpha, d, a respectively: ").split()
  values.extend([sp.radians(int(theta)), sp.radians(int(aplha)), d, a])

values = [float(values[i]) for i in range(len(values))]
values = [round(values[i], 3) for i in range(len(values))]

print("DH Matrix is:")
print("THETA\tALPHA\td\ta")
print("--------------------------------")
for i in range(n):
  t = i*4
  print(values[t],'\t',values[t+1], '\t', values[t+2], '\t', values[t+3])
  rotate = np.array([[sp.cos(values[t]), -sp.sin(values[t])*sp.cos(values[t+1]), sp.sin(values[t])*sp.sin(values[t+1])],
                     [sp.sin(values[t]), sp.cos(values[t])*sp.cos(values[t+1]), -sp.cos(values[t])*sp.sin(values[t+1])],
                     [0, sp.sin(values[t+1]), sp.cos(values[t+1])]
                    ])

  trans = np.array([values[t+3]*sp.cos(values[t]), values[t+3]*sp.sin(values[t]), values[t+2]])
  scale = np.array([0, 0, 0, 1])
  m = np.column_stack((rotate, trans))
  matrix = np.vstack((m, scale))
  matrices.append(matrix)

for i in range(len(matrices)):
  z = np.matmul(temp, matrices[i])
  temp = z
  print("Matrix: ", str(i+1), str(i+2))
  print(matrices[i])

print("Final Transformation: ")
print(np.round(temp, decimals = 4))
