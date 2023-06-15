import numpy as np

x = int(input("KONFIGURACJA\nPodaj ilosc serdnii, ktore ma obliczac program\n"))
l = np.zeros(x, dtype=int)
p = 0
print("Wpisz dlugosc serdnii (podawaj malejaco, bez powtorek)...")
while p < x:
    l[p] = int(input("nr " + str(p+1) + ": "))
    p += 1
p = 0
m = np.zeros(l[0])
s = np.zeros(x)
s[x-1] = 0
print("Witaj w programie obliczajacym duzo serdnii !!! (najpierw musisz wpisac " + str(l[0]) + " wartosci !!!)")
p = l[0]
while p:
    p -= 1
    m[p] = float(input())
i = x
print("p - " + str(p))
while i > 1:
    i -= 1
    while p < l[i]:
        s[i-1] += m[p]
        p += 1
    s[i-1] = s[i]
while p < l[0]:
    s[0] += m[p]
    p += 1
i = x
while i:
    i -= 1
    print("Serdnia z " + str(l[i]) + " to " + str(s[i]/l[i]) + " !!!")
print("Swietnie !!! Teraz mozemy liczyc nowa serdnie po kazdej wpisanej wartosci !!!\nDawaj NAN")
while True:
    p = (p+l[0]-1)%l[0]
    s[0] -= m[p]
    m[p] = float(input())
    i = x
    while i:
        i -= 1
        s[i] += m[p] - m[(p+l[i])%l[0]]
        print("Serdnia z " + str(l[i]) + " to " + str(s[i]/l[i]) + " !!!")
    s[0] += m[p]
    print("Serdnia z " + str(l[0]) + " to " + str(s[0]/l[0]) + " !!!")
