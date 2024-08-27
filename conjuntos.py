numeros = {2,3,4,5,6,7,8,9,10}

numeros_escrito = set(["Uno", "Dos", "Tres"])
##crear conjunto
numeros.add(15)

##elimina los conjuntos
##numeros.clear()

##elimina cualquier elementos
##numeros.pop()

##elimina un elemento especifico 
##numeros.remove(5)

##La union de dos conjuntos
todo = numeros.union(numeros_escrito)

print(todo)