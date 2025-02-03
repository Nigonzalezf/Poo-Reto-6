def prime_numbers(n):
    # Verificación de si el número es primo o no
    if n < 2:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True

def select_primes(num_list):
    primes = [n for n in num_list if prime_numbers(n)]
    return primes

# Le pedimos al usuario los números a evaluar
try:
    entry = input("Ingresar la lista de números separados por espacios: ")

    # Convertir la entrada en una lista de enteros
    num_list = list(map(int, entry.split()))

    # Seleccionar los números primos
    primes_list = select_primes(num_list)

    # Mostrar los resultados
    print("Lista original:", num_list)
    print("Números primos:", primes_list)

except ValueError as e:
    print("Error: Asegúrate de ingresar solo números enteros separados por espacios.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)
