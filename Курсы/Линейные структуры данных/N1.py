#...

m = []
go = True
while go:
    match input().split():
        case ["push", n]:
            m.append(int(n))
            print("ok")
        case ["pop"]:
            m.pop(-1)
            print("ok")
        case ["back"]:
            print(m[-1])
        case ["size"]:
            print(len(m))
        case ["clear"]:
            m.clear()
            print("ok")
        case ["exit"]:
            go = False