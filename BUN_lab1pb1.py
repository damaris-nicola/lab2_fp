# determinarea unei zile calendaristice (an, luna, zi) pornind de la
# doua numere intregi care reprezinta anul si numarul de ordine al zilei
# din anul respectiv


def verificare_an_bisect(an):
    return an % 4 == 0


def get_days_in_month(luna, bisect):
    feb_days = 28
    if bisect:
        feb_days += 1
    return {
        'ianuarie': 31,
        'februarie': feb_days,
        'martie': 31,
        'aprilie': 30,
        'mai': 31,
        'iunie': 30,
        'iulie': 31,
        'august': 31,
        'septembrie': 30,
        'octombrie': 31,
        'noiembrie': 30,
        'decembrie': 31
    }[luna]


def afisare_data(an, luni_an, zi):
    print("Anul:{}  Luna:{}  Ziua:{}".format(an, luni_an, zi))


def determinare_luna_zi(ord_zi, an):
    luni_an = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie',
               'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie',
               'decembrie']

    bisect = verificare_an_bisect(an)
    total_zile_luna = 0
    for luna in luni_an:
        total_luna_precedenta = total_zile_luna
        total_zile_luna += get_days_in_month(luna, bisect)
        if ord_zi < total_zile_luna:
            afisare_data(an, luna, ord_zi - total_luna_precedenta)
            break


def main():
    print("Dati anul si numarul de ordine al zilei")
    an = int(input("an="))
    ord_zi = int(input("numarul de ordine al zilei="))
    determinare_luna_zi(ord_zi, an)


if __name__ == "__main__":
    main()
