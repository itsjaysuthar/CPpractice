# ---------------------------------------------------------------------------------------
# -------------------Author : itsjaysuthar ----------------------------------------------
# ---------------------------------------------------------------------------------------

l=[]  #paste given list here 
l = sorted(l)
dict = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
    "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
    "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
    "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
    "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
    "Z": 26
}
sumf = 0
for i in range(0, len(l)):
    sum = 0
    for j in range(0, len(l[i])):
        m = l[i][j]
        k = dict[m]
        sum = sum + k
    sumf = sumf + (sum * (i+1))

print(sumf)
