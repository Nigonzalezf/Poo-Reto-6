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
