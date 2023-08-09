import math
class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return distancia

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        print("Punto movido a nuevas coordenadas.")


if __name__ == "__main__":
   p1:Punto = Punto (2,5)
   p2:Punto = Punto (4,7)
print("Punto1",p1.x,p1.y)
print("Punto2",p2.x,p2.y)

# Crear instancias de la clase Punto
p1 = Punto(3, 4)
p2 = Punto(0, 0)

# Mostrar coordenadas de punto1
p1.mostrar()

# Mover punto1 a nuevas coordenadas
p1.mover(6, 8)
p1.mostrar()

# Calcular distancia entre punto1 y punto2
distancia = p1.calcular_distancia(p2)
print(f"Distancia entre punto1 y punto2: {distancia}")
