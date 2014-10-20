# determinarea unei zile calendaristice (an, luna, zi) pornind de la
# doua numere intregi care reprezinta anul si numarul de ordine al zilei
# din anul respectiv


def verify_leap_year(year):
    """
    Verify if an year is a leap year
    :param year:int
    :return:bool
    """
    return year % 4 == 0


def get_days_in_month(month, leap_year):
    """
    Generate days in month.
    :param month: string
    :param bisect: int
    :return: int
    """
    feb_days = 28
    if leap_year:
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
    }[month]


def date_display(year, years_month, day):
    """
    Print the calendar date on the screen.
    :param year:int
    :param years_month:str
    :param day:int
    :return:
    """
    print("Anul:{}  Luna:{}  Ziua:{}".format(year, years_month, day))


def get_date(nr_of_the_day, year):
    """
    Return the calendar date for the input day and year.
    :param nr_of_the_day:int
    :param year:int
    :return:
    """
    years_month = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie',
               'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie',
               'decembrie']

    leap_year = verify_leap_year(year)
    total_days_month = 0
    for month in years_month:
        total_previous_month = total_days_month
        total_days_month += get_days_in_month(month, leap_year)
        if nr_of_the_day < total_days_month:
            date_display(year, month, nr_of_the_day - total_previous_month)
            break


def main():
    print("Dati anul si numarul de ordine al zilei")
    year = int(input("an="))
    nr_of_the_day = int(input("numarul de ordine al zilei="))
    get_date(nr_of_the_day, year)


if __name__ == "__main__":
    main()
