n = int(input())

#gg

l = []
arr = []
for i in range(n):
    arr.append(int(input()))

for i in arr:
    arr[arr.index(i)] = 100001
    if i not in arr:
        l.append(i)

    arr[arr.index(100001)] = i

try:
    print(min(l))
except:
    print(-1)