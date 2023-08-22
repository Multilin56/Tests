a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

#gg

answer = 0
for i in range(b-a+1):
    if ((a+i) % 2 != 0):
        answer += 1

print(answer)