# Poo-Reto-6
## Parte 1
1. Se crea la función `basic_operations` en donde mediante condicionales se ejecutan sumas, restas, multiplicaciones y divisiones. Mediante las excepciones se evita las indeterminaciones.
```python
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
```

2. Mediante la función `palindromo`, se toma la palabra ingresada, se convierten todas las letras en minúsculas, luego se calcula el largo de la palabra y se realiza una comparación de carácter por carácter. Con las excepciones evitamos que la entrada este vacia. 
```python
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
```

3. En este caso fue propuesto el uso de dos funciones, la primera utilizada para la verificación de que cada numero es o no es primo, y la segunda es utilizada para crear una lista con los numeros que si cumplen con la condición. El uso de excepciones verifica que el usuario haya digitado correctamente los numeros a verificar.
```python
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
```
 4. En este ejercicio es importante verificar inicialmente, si la lista cuenta con mas de dos elementos para poder efectuar una suma, en ese caso, el programa imprime un mensaje que aclara que no es posible seguir con el proceso. Seguido de esto se realizan diversas sumas de todos los pares consecutivos encontrados en la lista, y se comparan entre si para encontrar el resultado mas grande.
```python
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
```

5. Cada candena (palabra) es ordenada para asi crear claves y compararlas entre si. Las cadenas que cuenten con la misma clave, son seleccionadas para la creacion de una lista que es mostrada en la salida del programa.
```python
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
```

## Parte 2
Para la realización de esta parte del reto, se toma el paquete `shapes`, y se le implementan las distintas excepciones que se consideren pertinentes en las clases pertenecientes a cada figura.
```python
import math

class ShapeError(Exception):
    # Excepción personalizada para errores relacionados con figuras geométricas
    pass

class Shape:
    def area(self):
        raise NotImplementedError("El método 'area' debe ser implementado por las subclases")
    def perimeter(self):
        raise NotImplementedError("El método 'perimeter' debe ser implementado por las subclases")

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ShapeError("El radio debe ser un número positivo.")
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ShapeError("El ancho y el alto deben ser números positivos.")
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ShapeError("Los lados del triángulo deben ser números positivos.")
        # Validación: los lados deben cumplir la desigualdad triangular
        if a + b <= c or a + c <= b or b + c <= a:
            raise ShapeError("Los lados proporcionados no forman un triángulo válido.")
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2  
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c

# Ejemplo de uso con manejo de excepciones
try:
    c = Circle(-5)  # Esto generará una excepción
except ShapeError as e:
    print(f"Error: {e}")

try:
    t = Triangle(3, 4, 10)  # Esto también generará una excepción
except ShapeError as e:
    print(f"Error: {e}")
```
