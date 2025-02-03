def palindromo(palabra):
    # Se convierte a minúsculas y se eliminan espacios
    palabra = palabra.lower().replace(" ", "")
    # Comparar la palabra con su reverso
    return palabra == palabra[::-1]

# Se solicita al usuario ingresar una palabra
try:
    entrada = input("Ingresa una palabra: ")

    # Verificamos que la entrada no esté vacía
    if not entrada:
        raise ValueError("La entrada no puede estar vacía.")

    # Se verifica si es palíndromo
    if palindromo(entrada):
        print(entrada, "es un palíndromo.")
    else:
        print(entrada, "no es un palíndromo.")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
