# pentru un numar natural n dat gasiti numarul natural minim format cu aceleasi cifre


def numbers_digit(n):
    """
    Extrage cifrele unui numar intr-o lista, si sorteaza lista crescator
    :param n: int
    :return:list
    """
    L = []
    while (n > 0):
        L.append(n % 10)
        n = n // 10
    L.sort()
    return L


def get_number(L):
    """
    Formeaza numarul folosind lista sortata si puterile lui 10
    :param L: list
    :return: int
    """
    lungime = len(L)
    nr = 0
    for i in range(lungime):
        nr = nr + (L[i]) * 10 ** (lungime - i - 1)
    return nr

if __name__ == "__main__":
    print("Dati numarul n dorit")
    n = int(input("n="))
    L = []
    L = numbers_digit(n)
    minim = get_number(L)
    print("Numarul minim format cu aceleasi cifre este: ", minim)
