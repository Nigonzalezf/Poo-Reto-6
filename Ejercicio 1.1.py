def basic_operations(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("No es posible hacer la división entre cero")  # Lanzar una excepción
        else:
            return a / b
    else:
        raise ValueError("Operador no válido. Debe ser '+', '-', '*' o '/'")  # Lanzar una excepción

try:
    operation = input("Ingrese la operación (+, -, *, /): ")
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    
    result = basic_operations(a, b, operation)
    print("El resultado es:", a, operation, b, "=", result)

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
