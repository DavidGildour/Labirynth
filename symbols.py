#IN ORDER TO ENNUMERATE GRIDS LARGER THAN 9 I NEEDED TO EXPAND THE DIGITS
#'VOCABULARY'. SO NOW AFTER 9 THERE GOES ALL THE ALPHABET.
SYMBOLS = '0123456789abcdefghijklmnopqrstuvwyz'

def symbls():
    symbols = '0123456789abcdefghijklmnopqrstuvwyz'
    rows = []
    columns =[]
    for i in range(len(symbols)):
        rows.append(symbols[i])
        columns.append(symbols[i])
    return symbols, rows, columns
