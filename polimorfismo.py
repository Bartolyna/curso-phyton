class Gato():
    def sonido(self):
        print("MIAU")

class Perro():
    def sonido(self):
        print("GUAU")
        
def escucharSonido(animal):
    animal.sonido()
    
gato1 = Gato()
perro1 = Perro()

escucharSonido(gato1)