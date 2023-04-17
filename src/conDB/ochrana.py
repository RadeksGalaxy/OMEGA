import re


def sql_injection(vstup):
    """
    metoda pro kontrolu sql injaction
    :param vstup: vtupni textovy retezec
    :return: true=nesplnuje sql injaction false= splnuje
    """
    regX = '^[^\'\";]*$'  # kontroluje ' a " a ;
    regX2 = '^(?!.*--).*$'  # kontroluje aby neslo neco zapoznamkovat
    if not re.match(regX, vstup) or not re.match(regX, str(id)) and not re.match(regX2, vstup) or not re.match(regX2,
                                                                                                               str(id)):
        return True
    else:
        return False
