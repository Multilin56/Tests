#...

m = []
for i in input().split():
    match i:
        case "+":
            t = int(m[len(m) - 2]) + int(m[-1])
            m.pop(-1)
            m.pop(-1)
            m.append(t)
        case "-":
            t = int(m[len(m) - 2]) - int(m[-1])
            m.pop(-1)
            m.pop(-1)
            m.append(t)
        case "*":
            t = int(m[len(m) - 2]) * int(m[-1])
            m.pop(-1)
            m.pop(-1)
            m.append(t)
        case _:
            m.append(i)

for i in range(len(m)-1):
    t = int(m[len(m) - 2]) + int(m[-1])
    m.pop(-1)
    m.pop(-1)
    m.append(t)

print(m)
print(m[0])