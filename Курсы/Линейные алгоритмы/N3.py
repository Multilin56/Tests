n, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#gg

ai = 0
bi = 0
for i in range(n):
    if b[bi] <= b[i]:
        bi = i
    if a[ai] > a[i]:
        ai = i

if ai > bi:
    print(x)
    print(-1, -1)
else:
    print((x // a[ai]) * b[bi] + x % a[ai])
    print(ai + 1, bi + 1)