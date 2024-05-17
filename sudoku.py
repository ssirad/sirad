def controlla_righa(riga, num):
    if str(num) in riga:
        return False
    return True

def controlla_colonna(lista_tot, col, num):
    for i in range(9):
        if str(num) == lista_tot[i][col]:
            return False
    return True

def controllo_casellone(lista_tot, start_row, start_col, num):
    for i in range(3):
        for j in range(3):
            if str(num) == lista_tot[start_row + i][start_col + j]:
                return False
    return True

def risolvi_sudoku(lista_tot):
    for i in range(9):
        for j in range(9):
            if lista_tot[i][j] == '0':
                for num in range(1, 10):
                    if (controlla_righa(lista_tot[i], num) and
                        controlla_colonna(lista_tot, j, num) and
                        controllo_casellone(lista_tot, i - i % 3, j - j % 3, num)):
                        lista_tot[i][j] = str(num)
                        if risolvi_sudoku(lista_tot):
                            return True
                        lista_tot[i][j] = '0'
                return False
    return True


def stampa_sudoku(lista_tot):
    for riga in lista_tot:
        print(" ".join(riga))

lista_tot = []
for k in range(9):
    q = input("Scrivi tutti i numeri della riga con uno spazio: ")
    lista_tot.append(q.split())

if risolvi_sudoku(lista_tot):
    stampa_sudoku(lista_tot)
else:
    print("Non è possibile risolvere questo Sudoku.")
