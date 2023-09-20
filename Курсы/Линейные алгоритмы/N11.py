n, k = map(int, input().split())
m = list(map(int, input().split()))

#...

i_best = -1
j_best = -1
hmm = 0

k_arr = []
for i in range(1, k + 1):
    k_arr.append(i)

stage_1 = True
stage_2 = True
go = True
while go:
    if stage_1:
        print(i_best, j_best)
        j_best += 1
        for i in k_arr:
            if i in m[i_best:j_best]:
                hmm += 1

        if hmm == k:
            stage_1 = False

    elif stage_2:
        i_best += 1
        for i in k_arr:
            if i not in m[i_best:j_best]:
                hmm += 1

        if hmm == k:
            stage_2 = False

    else:
        go = False

print(i_best, j_best)