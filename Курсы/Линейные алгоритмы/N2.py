NK = list(int(i) for i in input().split())
N = list(int(i) for i in input().split())

#gg

N1 = N.index(max(N))
N2 = 0
N[N1] = 0

arr = []
for i in range(NK[1]*2+1):
    arr.append(N1-NK[1]+i)

for i in N:
    if i > N2 and N.index(i) != arr:
        N2 = N.index(i)
    else:
        N[N.index(i)] = 0

if N1 < N2:
    print(N1+1, N2+1)
else:
    print(N2+1, N1+1)

print(N)

for i in N:
    a = i
    for i in N.index(i):
        b = N[i]
N2 = N.index(max(N))

print(N)

if N1 < N2:
    print(N1+1, N2+1)
else:
    print(N2+1, N1+1)