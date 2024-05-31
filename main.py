import numpy as np

def gauss_solver(A, b) -> np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]]:
    n: int = len(A)

    # Etapa de escalonamento
    for i in range(n):
        max_el: int = abs(A[i][i])
        max_row: int = i
        for k in range(i+1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k

        A[[i, max_row]] = A[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]

        for k in range(i+1, n):
            factor = A[k][i]/A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]

            b[k] -= factor * b[i]

    # Substituição para trás
    x: np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]] = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i]/A[i][i]
        for k in range(i-1, -1, -1):
            b[k] -= A[k][i] * x[i]

    return x

# Definindo a matriz de coeficientes
A: np.ndarray[np.Any, np.dtype[np.Any]] = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)

# Definindo o vetor de termos constantes
b: np.ndarray[np.Any, np.dtype[np.Any]] = np.array([1, -2, 0], dtype=float)

# Resolvendo o sistema linear
x = gauss_solver(A, b)

print('Solução do sistema linear:', x)