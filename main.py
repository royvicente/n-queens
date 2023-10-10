def is_safe(board, row, col, n):
    # Verifica la fila hacia la izquierda
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Verifica la diagonal superior izquierda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Verifica la diagonal inferior izquierda
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, n):
    # Función recursiva para resolver el problema de las N reinas
    
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0
    
    return False

def solve_n_queens(n):
    # Función principal para resolver el problema de las N reinas
    
    board = [[0] * n for _ in range(n)]
    
    if not solve_n_queens_util(board, 0, n):
        print("No se encontró solución.")
        return
    
    # Imprimir la solución
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

# Ejemplo de uso
n = 8  # Cambiar el valor de N según el tamaño del tablero
solve_n_queens(n)
