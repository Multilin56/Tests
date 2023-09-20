n = int(input("Введите размер доски: "))

#gg

arr = {}
answer = {}
for i in range(n):
    x = int(input("Позиция: "))
    arr[i] = [x, i+1]

print(arr)
for i in range(n):
    # if (arr[i][1] < (1 + n) / 2):
    #     answer[i] = [arr[i][1], abs(arr[i][0]-n-1)]

    if (arr[i][0] > (1+n)/2 and arr[i][1] < (1+n)/2):
        arr[i][1] = abs(arr[i][1] - n - 1)
        c = arr[i][0]
        arr[i][0] = arr[i][1]
        arr[i][1] = c

        answer[i] = [abs(arr[i][1]-n-1), arr[i][0]]
    else:
        # arr[i][0] = abs(arr[i][0] - n - 1)

        c = arr[i][1]
        arr[i][1] = arr[i][0]
        arr[i][0] = abs(c - n - 1)

    # c = arr[i][0]
    # arr[i][0] = arr[i][1]
    # arr[i][1] = abs(c - n - 1)

    # if (arr[i][0] > (1+n)/2 and arr[i][1] < (1+n)/2):
    #     arr[i][1] = abs(arr[i][1] - n - 1)
    #     c = arr[i][0]
    #     arr[i][0] = arr[i][1]
    #     arr[i][1] = c
    # else:
    #     # arr[i][0] = abs(arr[i][0] - n - 1)
    #
    #     c = arr[i][1]
    #     arr[i][1] = arr[i][0]
    #     arr[i][0] = abs(c - n - 1)

    # if (arr[i][0] > (1+n)/2):
    #     c = arr[i][0]
    #     arr[i][0] = arr[i][1]
    #     arr[i][1] = abs(c - n - 1)
    # else:
    #     arr[i][0] = abs(arr[i][0] - n - 1)
    #     # c = arr[i][0]
    #     # arr[i][0] = arr[i][1]
    #     # arr[i][1] = c

print(answer)