#---------------------------------------------------------------------------------------
#-------------------Author : itsjaysuthar ----------------------------------------------
#---------------------------------------------------------------------------------------


t = int(input())
if 1 <= t <= 1000:
    def fact(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * fact(n - 1)


    f = []
    i = 0
    while i < t:
        x = int(input())
        if 0 <= x <= 20:
            f.append(fact(x))

        i += 1

    for i in range(0, len(f)):
        print(f[i])