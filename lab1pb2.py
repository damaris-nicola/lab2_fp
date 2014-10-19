# pentru un numar natural n dat gasiti numarul natural minim format cu aceleasi cifre


def cifre_numar(n):
    L = []
    while (n > 0):
        L.append(n % 10)
        n = n // 10
    return L


def formare_numar(L):
    lungime = len(L)
    nr = 0
    for i in range(lungime):
        nr = nr + (L[i]) * 10 ** (lungime - i - 1)
    return nr

if __name__ == "__main__":
    print("Dati numarul n dorit")
    n = int(input("n="))
    L = []
    L = cifre_numar(n)
    L.sort()
    minim = formare_numar(L)
    print("Numarul minim format cu aceleasi cifre este: ", minim)
