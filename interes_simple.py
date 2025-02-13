def calcular_interes_simple(m, i, t):
    return (m * i * t) / 100  # Usamos los nombres correctos de los parámetros

# Pedir datos antes de llamar la función
m = float(input("Ingrese el monto: "))
i = float(input("Introduzca la tasa de interés por año (%): "))
t = float(input("Ingresa el periodo de tiempo en años: "))

# Calcular el interés
interes = calcular_interes_simple(m, i, t)

# Mostrar el resultado
print(f"El interés simple es: {interes}")
