"""7-Eleven function."""


def print_7_eleven(number):
    """print 7-eleven."""
    if number%7 == 0 and number%11 == 0:
        return "7-Eleven"
    if number%7 == 0:
        return "Seven"
    elif number%11 == 0:
        return "Eleven"
    else:
        return number