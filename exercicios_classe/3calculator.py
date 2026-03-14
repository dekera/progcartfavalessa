class Calculator():
    def __init__(self,x1:float,x2:float):
        self.x1 = x1
        self.x2 = x2
    def soma (self):
        return self.x1+self.x2
    def subtracao (self):
        return self.x1 - self.x2
    def multiplicacao (self):
        return self.x1*self.x2
    def divisao (self):
        if self.x2 != 0:
            return self.x1/self.x2
        else:
            return("Não é possível dividir por zero!")
    
if __name__ == "__main__":
    numeros = Calculator(1,0)
    print(numeros.soma())
    print(numeros.subtracao())
    print(numeros.multiplicacao())
    print(numeros.divisao())