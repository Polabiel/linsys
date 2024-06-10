from typing import Any, Literal
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import dtype, floating, ndarray
from scipy.optimize import linprog
from scipy.optimize._optimize import OptimizeResult

def problem_1():
    
    """
    minimizar: 5x_1 + x_2
    sujeito a 2x_1 + x_2 ≥ 6
    x_1 + x_2 ≥ 4
    x_1 + 5x_2 ≥ 10
    x_1, x_2 ≥ 0
    
    A solução ótima deste problema é x^∗ = (0, 6) com f(x^∗) = 6.
    """
        
    # Coeficientes da função objetivo
    c: list[int] = [5, 1]

    # Matriz de coeficientes das desigualdades
    A: list[list[int]] = [[-2, -1], [-1, -1], [-1, -5]]

    # Vetor de termos independentes das desigualdades
    b: list[int] = [-6, -4, -10]

    # Limites para as variáveis
    x0_bounds: tuple[Literal[0], None] = (0, None)
    x1_bounds: tuple[Literal[0], None] = (0, None)

    res: OptimizeResult = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
    
    print_result(res)

def print_result(res: OptimizeResult) -> None:
    print("Resultado: ")
    print(f"x1 = {res.x[0]}")
    print(f"x2 = {res.x[1]}")
    print(f"Função objetivo = {res.fun}")
    print(f"Status = {res.status}")
    print(f"Mensagem = {res.message}")
    print(f"Iterações = {res.nit}")

if __name__ == "__main__":
    problem_1()