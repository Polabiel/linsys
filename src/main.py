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

def jacobian_solver(A, b, x0, tol=1e-6, max_iter=1000) -> np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]]:
    n: int = len(A)
    x: np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]] = x0

    for _ in range(max_iter):
        x_new: np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]] = np.zeros(n)
        for i in range(n):
            s: float = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new

    return x

def main() -> None:
    A: np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]] = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])
    b: np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]] = np.array([7, -8, 6])

    x_gauss: np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]] = gauss_solver(A, b)
    x_jac: np.ndarray[np.Any, np.dtype[np.floating[np._64Bit]]] = jacobian_solver(A, b, np.zeros(3))

    print(x_gauss)
    print(x_jac)