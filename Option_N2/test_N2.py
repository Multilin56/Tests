a = int(input("Введите колличество круасанов: "))
b = int(input("Введите колличество эклеров: "))

#gg

first_answer = 0
second_answer = 0
while(True):
    if (a > b):
        a -= 2
        b -= 1
        first_answer += 1
    else:
        a -= 1
        b -= 2
        second_answer += 1

    if ((a+b) % 3 != 0):
        print(-1)
        break
    elif (a == 0 and b ==0):
        print(str(first_answer) + " " + str(second_answer))
        break