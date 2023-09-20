#...

q = []
s = []
go = True
while go:
    match input().split():
        case ["push", n]:
            q = list(reversed(s))
            q.append(n)
            s = list(reversed(q))
            print("ok")
        case ["pop"]:
            s = list(reversed(q))
            s.pop(-1)
            q = list(reversed(s))
            print("ok")
        case ["front"]:
            s = list(reversed(q))
            q = list(reversed(s))
            print(q[0])
        case ["size"]:
            s = list(reversed(q))
            q = list(reversed(s))
            print(len(q))
        case ["clear"]:
            s.clear()
            q.clear()
            print("ok")
        case ["exit"]:
            go = False
            print("bye")