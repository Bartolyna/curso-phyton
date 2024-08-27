class Animales:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def walk(self):
        if self.age > 3 and self.weight > 10:
            return self.name + ' camina lento por su edad y su peso.'
        elif self.age > 2  and self.weight > 5:
            return self.name + ' camina a velocidad media por su edad y su peso.'
        else:
            return self.name + ' camina rapido por su edad y su peso.'
        
    def eat(self):
        if self.weight >= 1 and self.weight <= 3:
            return self.name + ' debe comer mejor.'
        elif self.weight >=4 and self.weight <= 6:
            return self.name + 'esta comiendo saludable.'
        else:
            return self.name + ' tiene que comer saludable.'

Perro = Animales("Miniti", 12, 15.4)
Gato = Animales("Michi", 5, 11.4)

print("Como esta la alimentacion de mi animal: " + str(Perro.eat()))