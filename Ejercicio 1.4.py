def higher_consecutive_add(num_list):
    if len(num_list) < 2:
        return False  # No hay suficientes elementos para sumar

    higher_add: float = 0

    for i in range(len(num_list) - 1):
        add = num_list[i] + num_list[i + 1]
        if add > higher_add:
            higher_add = add

    return higher_add

# Solicitar al usuario que ingrese una lista de números
try:
    entry = input("Ingrese la lista de números separados por espacios: ")

    # Convertir la entrada en una lista de enteros
    num_list = list(map(int, entry.split()))

    # Calcular la mayor suma entre dos elementos consecutivos
    result = higher_consecutive_add(num_list)

    # Mostrar el resultado
    if result is not False:
        print("La mayor suma entre dos elementos consecutivos es:", result)
    else:
        print("La lista debe tener al menos dos elementos.")

except ValueError as e:
    print("Error: Asegúrate de ingresar solo números enteros separados por espacios.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)
