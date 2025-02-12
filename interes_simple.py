def calcular_interes_simple(capital, tasa, tiempo):
    """
    Calcula el interés simple.
    
    :param capital: Monto inicial
    :param tasa: Tasa de interés (en decimal, ej. 0.05 para 5%)
    :param tiempo: Tiempo en años
    :return: Interés generado
    """
    return capital * tasa * tiempo

# Ejemplo de uso
if __name__ == "__main__":
    capital = 1000  # Monto en pesos
    tasa = 0.05  # 5% anual
    tiempo = 3  # 3 años
    interes = calcular_interes_simple(capital, tasa, tiempo)
    print(f"El interés simple es: {interes}")
