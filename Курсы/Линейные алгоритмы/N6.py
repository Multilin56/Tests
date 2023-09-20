n = int(input())
a = list(map(int, input().split()))

#gg

ans1 = 0
ans2 = 0
flag = False
for i in range(n):
    ii = i
    for i in range(n-ii):
        if ii+i - ii > ans2 - ans1 and sum(a[ii:ii+i+1]) % 3 == 0:
            ans1 = ii
            ans2 = ii+i
            flag = True

if flag:
    print(ans1+1, ans2+1)
else:
    print(-1)

# n = int(input())
# a = list(map(int, input().split()))
#
# #gg
#
# p = [0] * (n + 1)
# for i in range(1, n + 1):
#     p[i] = p[i - 1] + a[i-1]
# ibest = 0
# jbest = 0
# imin = 0
# k = 0
# for j in range(1, n + 1):
#     if p[j] < p[imin]:
#         imin =  j
#     if p[j] - p[imin] > p[jbest] - p[ibest] and (p[j] - p[imin]) % 3 == 0:
#         print(p[j] - p[imin])
#         jbest = j
#         ibest = imin
#         k += 1
# if k < 1:
#     print(-1)
# else:
#     print(ibest + 1, jbest)