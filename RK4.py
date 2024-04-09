import math

def runge_kutta(f, x0, y0, h, n):
    """
    Método de Runge-Kutta de cuarto orden para resolver una ecuación diferencial ordinaria (ODE)
    
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
        k1 = h * f(x, y)
        k2 = h * f(x + (h/2), y + (k1/2))
        k3 = h * f(x + (h/2), y + (k2/2))
        k4 = h * f(x + h, y + k3)
        y += ((k1 + (2*k2)) + ((2*k3) + k4)) / 6
        x += h
        points.append((x, y))
    return points

def differential_equation(x, y):
    return 2*x-3*y  # Función de ejemplo: dy/dx = 3x - 2y

def exact_solution(x):
    return (2*(3*x - 1))/9 + (41*math.exp(3-3*x))/9  # Solución exacta de la ecuación diferencial

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
    solution = runge_kutta(differential_equation, x0, y0, h, n)
    print("\nSolución usando el método de Runge-Kutta de cuarto orden:")
    print("x\t\tSolución Aproximada\t\tSolución Exacta\t\tError (%)")
    for point in solution:
        x_rounded = round(point[0], 5)  # Redondear a 5 decimales
        exact = exact_solution(x_rounded)  # Calcular la solución exacta con el valor redondeado de x
        error = calculate_error(point[1], exact)
        print(f"{x_rounded}\t\t{point[1]}\t\t\t{exact}\t\t{error:.5f}")

if __name__ == "__main__":
    main()
