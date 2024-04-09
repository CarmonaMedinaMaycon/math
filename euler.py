import math


def euler_method(f, x0, y0, h, n):
    """
    Método de Euler para resolver una ecuación diferencial ordinaria (ODE)
    
    Parámetros:
        - f: Función que define la ecuación diferencial dy/dx = f(x, y)
        - x0, y0: Condiciones iniciales
        - h: Tamaño del paso (step size)
        - n: Número de pasos
        
    Retorna:
        - Una lista de tuplas (x, y) que representan los puntos de la solución aproximada
    """
    points = [(x0, y0)]
    x = x0
    y = y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
        points.append((x, y))
    return points

def differential_equation(x, y):
    return x + (1/5)*y

def exact_solution(x0, y0, x):
    return -5*x - 25 + 22*math.exp(x/5)  # Solución exacta de la ecuación diferencial

def calculate_error(approx, exact):
    return abs((exact - approx) / exact) * 100

def get_input():
    x0 = float(input("Ingrese el valor inicial de x: "))
    y0 = float(input("Ingrese el valor inicial de y: "))
    h = float(input("Ingrese el tamaño del paso (h): "))
    n = int(input("Ingrese el número de pasos (n): "))
    return x0, y0, h, n

def main():
    x0, y0, h, n = get_input()
    solution = euler_method(differential_equation, x0, y0, h, n)
    print("\nSolución usando el método de Euler:")
    print("x\t\tSolución Aproximada\t\tSolución Exacta\t\t  Error")
    for point in solution:
        exact = exact_solution(x0, y0, point[0])
        error = calculate_error(point[1], exact)
        print(f"{round(point[0], 5)}\t\t{round(point[1], 5)}\t\t\t{round(exact, 5)}\t\t\t{round(error, 5)}")


if __name__ == "__main__":
    main()
