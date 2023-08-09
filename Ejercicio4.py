class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.esquina_superior_izquierdo = punto1
        self.esquina_inferior_derecho = punto2

    def calcular_lados(self):
        base = abs(self.esquina_inferior_derecho.x - self.esquina_superior_izquierdo.x)
        altura = abs(self.esquina_inferior_derecho.y - self.esquina_superior_izquierdo.y)
        return base, altura

    def perimetro(self):
        base, altura = self.calcular_lados()
        perimetro = 2 * (base + altura)
        return perimetro

    def area(self):
        base, altura = self.calcular_lados()
        area = base * altura
        return area

    def cuadrado(self):
        base, altura = self.calcular_lados()
        return base == altura

if __name__ == "__main__":
 p1 = Punto(33, 4)
 p2 = Punto(23, 5)


rectangulo = Rectangulo(p1, p2)


print("Perímetro:", rectangulo.perimetro())
print("Área:", rectangulo.area())


if rectangulo.cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")
