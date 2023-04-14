from datetime import datetime

def datumValidator(y,m,d):
    '''
    metoda pro zkontrolovani datumu jestli existuje
    :param y: rok
    :param m: mesic
    :param d: den
    :return: true pokud datum existuje a pokud ne tak false
    '''
    try:
        datum = f'{y}-{m}-{d}'
        datetime.strptime(datum, '%Y-%m-%d')
        return True
    except ValueError:
        return False
