a = int(input("Время работы первого прожектора:"))
b = int(input("Время работы второго прожектора:"))
c = int(input("Время работы третьего прожектора:"))

#gg

answer = 0
while(True):

    a -= 1
    answer += 1
    if (b == 0):
        break

    b -= 1
    answer += 1
    if (c == 0):
        break

    c -= 1
    answer += 1
    if (b == 0):
        break

    b -= 1
    answer += 1
    if (a == 0):
        break

print(answer)