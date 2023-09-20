a = int(input("Введите текущий год: "))
b = int(input("Введите смещение?: "))

#gg

if ((a+b) <= 0 and a > 0):
    answer = a+b-1
elif ((a+b) >= 0 and a < 0):
    answer = a+b+1
else:
    answer = a+b

print(answer)