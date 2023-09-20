k = int(input("Введите переодичность остоновок: "))
n = int(input("Введите пройденое расстояние: "))

#gg

hmm = 0
while(True):
    if (n > hmm):
        hmm += k
    else:
        break

print(min(hmm-n, abs(hmm-k-n)))