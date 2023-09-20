#...

m = []
for i in list(map(str, input())):
    print(i)
    print(m)
    print("------")
    match str(i):
        case "(" | "[" | "{":
            m.append(i)
        case ")" | "]" | "}":
            print("!!!")
            match i:
                case ")":
                    i = "("
                case "]":
                    i = "["
                case "}":
                    i = "{"

            print(i)
            print(m[-1])
            if m[-1] == i:
                m.pop(-1)

if len(m) == 0:
    print("yes")
else:
    print("no")