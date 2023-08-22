i = int(input("Введите количество опор: "))

#gg

first_answer = None
second_answer = None

first_answer_test = None
second_answer_test = None
test = False
o1 = int(input("опора?:"))
for i in range(i-1):
    i += 1
    o2 = int(input("опора?:"))

    if (o1 < o2 and first_answer_test == None):
        first_answer_test = i
    elif (o1 > o2 and first_answer_test != None):
        second_answer_test = i + 1
        test = True

    o1 = o2

    if (first_answer != None and second_answer != None and test == True):
        if (first_answer - second_answer < first_answer_test - second_answer_test):
            first_answer = first_answer_test
            second_answer = second_answer_test

            first_answer_test = None
            second_answer_test = None
            test = False

    elif (first_answer == None and second_answer == None and test == True):
        first_answer = first_answer_test
        second_answer = second_answer_test

        first_answer_test = None
        second_answer_test = None
        test = False

print(first_answer)
print(second_answer)