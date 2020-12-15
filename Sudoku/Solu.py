def intento(sudo, k, pos):
    for i in range(9):
        if sudo[pos[0]][i] == k:
            return False

    for i in range(9):
        if sudo[i][pos[1]] == k:
            return False

    esq_col = (pos[1]//3)*3
    esq_fil = (pos[0]//3)*3
    for i in range(esq_fil, esq_fil + 3):
        for j in range(esq_col, esq_col + 3):
            if sudo[i][j] == k:
                return False

    return True

def vacio(sudo):
    for i in range(9):
        for j in range(9):
            if sudo[i][j] == 0:
                return i,j
    return "Fin"

def solu(sudo):
    pos = vacio(sudo)
    if pos == "Fin":
        return True
    else:
        fil,col=pos

    for k in range(1,10):
        if intento(sudo, k, (fil,col)):
            sudo[fil][col] = k
            if solu(sudo):
                return sudo
            sudo[fil][col] = 0
    return False

if __name__ == "__main__":
  prueba=[[0, 0, 4, 0, 0, 3, 0, 0, 0],
          [8, 0, 0, 0, 9, 0, 0, 6, 0],
          [0, 0, 0, 0, 0, 8, 0, 0, 1],
          [0, 1, 3, 5, 0, 0, 0, 0, 0],
          [0, 0, 9, 0, 0, 0, 5, 0, 7],
          [0, 0, 0, 0, 0, 6, 0, 1, 0],
          [0, 6, 0, 7, 2, 0, 0, 5, 9],
          [0, 0, 0, 3, 0, 0, 1, 0, 0],
          [0, 7, 0, 0, 0, 9, 2, 0, 0]]
  print(solu(prueba))

