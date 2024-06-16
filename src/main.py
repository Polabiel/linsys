from typing import Literal
from scipy.optimize import linprog
from scipy.optimize import minimize, OptimizeResult
import numpy as np
from colorama import Fore, Style

def problem_1():
    
    """
    minimizar: 5x_1 + x_2
    sujeito a 2x_1 + x_2 ≥ 6
    x_1 + x_2 ≥ 4
    x_1 + 5x_2 ≥ 10
    x_1, x_2 ≥ 0
    
    A solução ótima deste problema é x^∗ = (0, 6) com f(x^∗) = 6
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
    
    print_result(res, "Problema 1", "A solução ótima deste problema é x^∗ = (0, 6) com f(x^∗) = 6")
    
def problem_2():
    """
    maximizar 2x_1 − 3x_2
    sujeito a x_1 + 2x_2 ≤ 6
    2x_1 − x_2 ≤ 8
    x_1, x_2 ≥ 0
    A solução ótima deste problema é x^* = (4, 0) com f(x^*) = 8
    """
    
    # Coeficientes da função objetivo
    c: list[int] = [-2, 3]

    # Matriz de coeficientes das desigualdades
    A: list[list[int]] = [[1, 2], [-2, 1]]

    # Vetor de termos independentes das desigualdades
    b: list[int] = [6, 8]

    # Limites para as variáveis
    x0_bounds: tuple[Literal[0], None] = (0, None)
    x1_bounds: tuple[Literal[0], None] = (0, None)

    res: OptimizeResult = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
    
    print_result(res, "Problema 2", "A solução ótima deste problema é x^* = (4, 0) com f(x^*) = 8")
    
def problem_3():
    """
    maximizar 15(x_1 + 2x_2) + 11(x_2 − x_3)
    sujeito a 3x_1 ≥ x_1 + x_2 + x_3
    0 ≤ x_j ≤ 1
    j = 1, 2, 3
    A solução ótima deste problema é x^* = (1, 1, 0) com f(x^*) = 56
    """
    
    # Coeficientes da função objetivo
    c: list[int] = [-15, -37, 11]

    # Matriz de coeficientes das desigualdades
    A: list[list[int]] = [[-2, -1, -1]]

    # Vetor de termos independentes das desigualdades
    b: list[int] = [0]

    # Limites para as variáveis
    x0_bounds: tuple[Literal[0], 1] = (0, 1)
    x1_bounds: tuple[Literal[0], 1] = (0, 1)
    x2_bounds: tuple[Literal[0], 1] = (0, 1)

    res: OptimizeResult = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')
    
    print_result(res, "Problema 3", "A solução ótima deste problema é x^* = (1, 1, 0) com f(x^*) = 56")
    
def problem_4():
    """
    minimizar 10(x_3 + x_4)
    sujeito a sum_{j=1}^{4} x_j = 400
    x_j - 2x_{j+1} ≥ 0 para j = 1, 2, 3
    x_j ≥ 0 para j = 1, 2, 3
    A solução ótima deste problema é x^* = (400, 0, 0, 0) com f(x^*) = 0.
    """ 
    # Coeficientes da função objetivo
    c: list[int] = [0, 0, 10, 10]

    # Matriz de coeficientes das desigualdades
    A: list[list[int]] = [[1, 1, 1, 1], [1, -2, 0, 0], [0, 1, -2, 0], [0, 0, 1, -2]]

    # Vetor de termos independentes das desigualdades
    b: list[int] = [400, 0, 0, 0]

    # Limites para as variáveis
    x0_bounds: tuple[Literal[0], None] = (0, None)
    x1_bounds: tuple[Literal[0], None] = (0, None)
    x2_bounds: tuple[Literal[0], None] = (0, None)
    x3_bounds: tuple[Literal[0], None] = (0, None)

    res: OptimizeResult = linprog(c, A_eq=A, b_eq=b, bounds=[x0_bounds, x1_bounds, x2_bounds, x3_bounds], method='highs')
    
    print_result(res, "Problema 4", "A solução ótima deste problema é x^* = (400, 0, 0, 0) com f(x^*) = 0")

def problem_5():
    """
    maximizar −5x_1 + 3(x_1 + x_3)
    sujeito a x_j + 1 ≤ x_{j+1} para j = 1, 2
    sum_{j=1}^{3} x_j = 12
    x_j ≥ 0 para j = 1, 2, 3
    A solução ótima deste problema é x^* = (0, 1, 11) com f(x^*) = 36.
    """
    
    # Coeficientes da função objetivo
    c: list[int] = [5, 0, 3]

    # Matriz de coeficientes das desigualdades
    A: list[list[int]] = [[-1, 1, 0], [0, -1, 1]]

    # Vetor de termos independentes das desigualdades
    b: list[int] = [-1, -1]

    # Limites para as variáveis
    x0_bounds: tuple[Literal[0], None] = (0, None)
    x1_bounds: tuple[Literal[0], None] = (0, None)
    x2_bounds: tuple[Literal[0], None] = (0, None)

    res: OptimizeResult = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')
    
    print_result(res, "Problema 5", "A solução ótima deste problema é x^* = (0, 1, 11) com f(x^*) = 36")
    
def problem_6():
    """
    O problema 6 não foi resolvido pois não foi especificado no enunciado
    """
    
    print_result(None, "Problema 6", "O problema 6 não foi resolvido pois não foi especificado no enunciado")
    
def problem_7():
    """
    maximizar 9x_{1} + 5x_{2}
    sujeito a sen(k/13)_x_{1} + cos(k/13)x_{2} ≤ 7 para j = 1, 2, ..., 13
    x_{1}, x_{2} ≥ 0
    A solução ótima deste problema é x^* = (0, 1, 11) com f(x^*) = 36
    """
    # Função objetivo 
    def objective(x):
        return -1 * (9 * x[0] + 5 * x[1])
    
    # Restrições
    constraints = []
    for k in range(1, 14):
        # Como é uma solução de otimização não linea (já que tem que usar seno e cosseno), não é possível usar a biblioteca do scipy (POR QUE NÃO TEMaaaaaaaaaaaaaaaa)
        constraints.append({'type': 'ineq', 'fun': lambda x, k=k: -1 * (np.sin(k/13) * x[0] + np.cos(k/13) * x[1] - 7)})
        
    # Limites para as variáveis
    bnds: tuple[tuple[Literal[0], None], tuple[Literal[0], None]] = ((0, None), (0, None))
    
    # Solução inicial
    x0: list[int] = [0, 0]
    
    res: OptimizeResult = minimize(objective, x0, constraints=constraints, bounds=bnds)
    
    print_result(res, "Problema 7", "A solução ótima deste problema é x^* = (0, 1, 11) com f(x^*) = 36")
    
def print_result(res, problem_title: str, solution_greet: str = "Solução ótima"):
    
    if(res == None):
        print(Fore.RED + f"O problema {problem_title} não foi resolvido pois não foi especificado no enunciado" + Style.RESET_ALL)
        print(Fore.GREEN + "-------------------------------------" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + f"{problem_title}" + Style.RESET_ALL)
        print(Fore.GREEN + "Resultado: " + Style.RESET_ALL)
        print(Fore.BLUE + f"x1 = {res.x[0]}" + Style.RESET_ALL)
        print(Fore.BLUE + f"x2 = {res.x[1]}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Função objetivo = {res.fun}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Status = {res.status}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Mensagem = {res.message}" + Style.RESET_ALL)
        print(Fore.RED + f"Iterações = {res.nit}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"{solution_greet}" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "Solução Adquirida = " + str(res.x) + Style.RESET_ALL)
        print(Fore.GREEN + "-------------------------------------" + Style.RESET_ALL)
if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()
    problem_7()