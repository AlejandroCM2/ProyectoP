class Vehiculo:

    def __init__(self,velocidad_maxima: int, kilometraje:int ):
        self.velocidad_maxima: int = velocidad_maxima
        self.kilometraje: int = kilometraje

if __name__ == "__main__":
   v1: Vehiculo = Vehiculo(120,5000)
   v2: Vehiculo = Vehiculo(150,3000)

   print(v1.velocidad_maxima)