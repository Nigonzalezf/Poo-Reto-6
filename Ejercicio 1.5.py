def same_characters(word_list):
    result = []
    groups = {}

    for word in word_list:
        # Ordenar los caracteres de la palabra para crear una clave
        key = ''.join(sorted(word))

        # Agrupar palabras que tienen la misma clave
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    # Filtrar solo los grupos que tienen más de un elemento
    for group in groups.values():
        if len(group) > 1:
            result.extend(group)

    return result

# Solicitar al usuario que ingrese una lista de cadenas
try:
    entry = input("Ingresa una lista de cadenas separadas por comas: ")

    # Convertir la entrada en una lista de strings
    chains_list = [chain.strip() for chain in entry.split(",")]

    # Obtener los anagramas
    result = same_characters(chains_list)

    # Mostrar el resultado
    if result:
        print("Los elementos que tienen los mismos caracteres son:", result)
    else:
        print("No se encontraron elementos que tengan los mismos caracteres.")

except Exception as e:
    print("Ocurrió un error inesperado:", e)
