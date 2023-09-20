a = int(input())
b = int(input())
c = int(input())

#gg

if (a - b == b - c):
    print(c + abs(a-b))
    print(4)
elif (a - b < b - c):
    print(a + abs(b-c))
    print(2)
else:
    print(a + abs(a-b))
    print(3)