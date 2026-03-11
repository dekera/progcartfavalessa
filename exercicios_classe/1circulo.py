import numpy as np

class Circle():
    def __init__(self, raio:float):
        self.raio = raio
    def area(self):
        return np.pi * np.square(self.raio)
    def perimetro(self):
        return 2 * np.pi * self.raio
    
if __name__ == "__main__":
    circulo = Circle(1)
    print(circulo.area(), "\n")
    print(circulo.perimetro(), "\n")