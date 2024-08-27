def identidad(**kwargs):
    for k in kwargs:
        print(f'El nombre es {kwargs[k]}')
    
identidad(nombre = "Carlos", apellidos = "Rodriguez", edad ="25")