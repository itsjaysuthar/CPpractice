# ---------------------------------------------------------------------------------------
# -------------------Author : itsjaysuthar ----------------------------------------------
# ---------------------------------------------------------------------------------------
import math

a=[]
for i in range(2,101):
    for j in range(2,101):
        a.append(pow(i,j))


print(len(set(a)))