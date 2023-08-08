class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def cambiar(self):
        self.x: int = x
        self.y: int = y

if __name__ == "__main__":
   p1:Punto = Punto (2,5)
   p2:Punto = Punto (4,7)
print("Punto1",p1.x,p1.y)
print("Punto2",p2.x,p2.y)

   p1.cambiar(4,8)
   p2.cambiar(8,9)
print("NuevoPunto1", p1.cambiar)
print("NuevoPunto2", p2.cambiar)

