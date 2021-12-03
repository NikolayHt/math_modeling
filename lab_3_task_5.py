import numpy as np
N = 6
M = 5
NxM = np.zeros((N,M))
for i in range(N):
  for j in range(M):
    if i == 0 and j == 0:
      NxM[i,j] = np.sin(N * (i+1) + M * (j + 1))
    else:
      NxM[i,j] = np.sin(N * i + M * j)
    if NxM[i,j]<0: 
      NxM[i,j] = 0
print(NxM)      
a1 = 1
a2 = 2
for i in range(N):
  NxM[i][a1], NxM[i][a2] = NxM[i][a2], NxM[i][a1]
print(NxM)