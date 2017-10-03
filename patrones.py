import sys

class Gestor:
    def __init__(self):
        self.datos = []
        self.entradas = []

    def add(self, cine,pelicula_id, pelicula, funciones):
        self.datos.append([cine, Pelicula(pelicula_id, pelicula), funciones])

    def listar_peliculas(self, cine):
        for dato in self.datos:
            if dato[0].nombre == cine:
                print("{} {}".format(dato[1].id, dato[1].nombre))

    def listar_funciones(self, pelicula_id, cine):
        for dato in self.datos:
            if str(dato[1].id) == pelicula_id and dato[0].nombre == cine:
                for funcion in dato[2]:
                    print(funcion)
    def guardar_entrada(self, pelicula_id, funcion_elegida, cantidad, cine):
        self.entradas.append(Entrada(pelicula_id, funcion_elegida, cantidad, cine))

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad, cine):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad
        self.cine = cine

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

class CineFactory:
    def get_cine(self, nombre):
        if nombre == "CinePlaneta":
            return CinePlaneta(nombre)
        elif nombre == "CineStark":
            return CineStark(nombre)
        else:
            return None

class CinePlaneta:
    def __init__(self, nombre):
        self.nombre = nombre

class CineStark:
    def __init__(self, nombre):
        self.nombre = nombre

def main():
    factory = CineFactory()
    gestor = Gestor()
    gestor.add(factory.get_cine("CinePlaneta"), 1, "Desaparecido", ["20:00", "23:00"])
    terminado = False;
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

        elif opcion == '2':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = "CinePlaneta"
            elif cine == '2':
                cine = "CineStark"

            print('********************')
            gestor.listar_peliculas(cine)
            print('********************')

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = "CinePlaneta"
            elif cine == '2':
                cine = "CineStark"

            gestor.listar_peliculas(cine)
            pelicula_elegida = input('Elija pelicula:')
            #pelicula = obtener_pelicula(id_pelicula)
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            gestor.listar_funciones(pelicula_elegida, cine)
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = str(pelicula_elegida) + str("2017") + str(pelicula_elegida)
            gestor.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas, cine)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        elif opcion == '0':
            terminado = True
        else:
            print(opcion)



if __name__ == '__main__':
    main()
