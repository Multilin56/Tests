# n, k, m = map(int, input().split())
# a = list(map(int, input().split()))
#
# #gg
#
# p = [0] * (n+k)
# for i in range(1, n-1):
#     p[i] = a[i-k] + p[i-1]
#
#
# print(p)
# try:
#     print(p.index(m)-1)
# except:
#     print(0)

n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
flag = True
for i in range(len(arr) - k):
    if sum(arr[i:i + k + 1]) == m:
        print(i + 1)
        flag = False
        break
if flag:
    print(0)
