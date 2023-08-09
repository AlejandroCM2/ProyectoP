import math
class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        area = math.pi * (self.radio ** 2)
        return area

    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_pertenece(self, punto):
        distancia_centro = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia_centro <= self.radio

if __name__ == "__main__":
   centro_circulo = Punto(0, 6)


   circulo = Circulo(centro_circulo, 5)


   print("Área:", circulo.area())
   print("Perímetro:", circulo.perimetro())


   punto_verificar = Punto(3, 4)

   if circulo.punto_pertenece(punto_verificar):
    print("El punto pertenece al círculo.")
   else:
    print("El punto no pertenece al círculo.")
