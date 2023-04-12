from datetime import datetime

def datumValidator(y,m,d):
    try:
        datum = f'{y}-{m}-{d}'
        datetime.strptime(datum, '%Y-%m-%d')
        return True
    except ValueError:
        return False
