n = int(input())
a = list(map(int, input().split()))

#gg

ai = 0
aj = n-1
for i in range(n):
    if a[i] < a[ai] and i < aj:
        ai = i
    if a[i] > a[aj] and i > ai:
        aj = i

if a[aj] / a[ai] > 1:
    print(ai+1, aj+1)
else:
    print(0, 0)