# ---------------------------------------------------------------------------------------
# -------------------Author : itsjaysuthar ----------------------------------------------
# ---------------------------------------------------------------------------------------
a=[]
for i in range(1,5000):
    p=(i*(3*i-1))//2
    a.append(p)
b=[]
for j in range(len(a)):
    for k in range(len(a)):
        if (a[j]+a[k] in a):
            if a[j]>a[k]:
                if (a[j] - a[k] in a):
                    b.append(a[j]-a[k])
            else:
                if (a[k] - a[j] in a):
                    b.append(a[k]-a[j])

print(min(b))