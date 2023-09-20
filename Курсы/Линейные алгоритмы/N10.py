ni = int(input())
mi = list(map(int, input().split()))

nj = int(input())
mj = list(map(int, input().split()))

#...

i = 0
j = 0
i_best = 0
j_best = 0
summ = 10**5
go = True
while go:
    if abs(mi[i]-mj[j]) < summ:
        summ = abs(mi[i]-mj[j])
        i_best = mi[i]
        j_best = mj[j]

    if mi[i] == mj[j]:
        go = False
    elif mi[i] < mj[j]:
        i += 1
        if i >= ni:
            go = False
    else:
        j += 1
        if j >= nj:
            go = False

print(i_best, j_best)