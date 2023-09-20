n, r = map(int, input().split())
d = list(map(int, input().split()))

#...

i = 0
j = 0
ans = 0
go = True
while go:
    if d[j] - d[i] > r:
        ans += len(d[j:])
        i += 1
    else:
        j += 1
        if j >= n:
            go = False

print(ans)