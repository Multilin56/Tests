import math

s = int(input("Введите макс. размер щита: "))
i = int(input("Введите количество досок: "))

#gg

hmm = 0
hmhmm = 0
ahamm = 0
answer = 0
for i in range(i):
    a = int(input("доска?:"))
    ahamm -= 1
    if (a == 1 and ahamm <= 0):
        ahamm = s
        hmhmm += 1
    else:
        answer += math.ceil(hmhmm/s)
        hmhmm = 0
else:
    answer += math.ceil(hmhmm/s)

print(answer)