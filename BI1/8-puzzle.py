import busquedas

class modelo8Puzzle(busquedas.modeloBusqueda):
    """
    El problema del 8 puzzle.
    El estado es una lista de 10 números, donde el 0 es el espacio vacío.
    """
    def __init__(self):
        self.acciones = {0: ['D', 'R'],
                         1: ['D', 'R', 'L'],
                         2: ['D', 'L'],
                         3: ['U', 'D', 'R'],
                         4: ['U', 'D', 'R', 'L'],
                         5: ['U', 'D', 'L'],
                         6: ['U', 'R'],
                         7: ['U', 'R', 'L'],
                         8: ['U', 'L']}

    def acciones_legales(self, estado):
        return self.acciones[estado[-1]]

    def sucesor(self, estado, accion):
        s = list(estado)
        ind = s[-1]
        bias = (-3 if accion is 'U' else
                3 if accion is 'D' else
                -1 if accion is 'L' else
                1)
        s[ind], s[ind + bias] = s[ind + bias], s[ind]
        s[-1] += bias
        return tuple(s)

    def dibuja(estado):
        cadena = "-------------\n"
        for i in range(3):
            for j in range(3):
                if estado[3 * i + j] > 0:
                    cadena += "| " + str(estado[3 * i + j]) + " "
                else:
                    cadena += "|   "
            cadena += "|\n-------------\n"
        return cadena


class ochoPuzzle(busquedas.problemaBusqueda):
    def __init__(self, pos_ini, pos_meta=None):
        if pos_meta is None:
            pos_meta = (0, 1, 2, 3, 4, 5, 6, 7, 8, 0)
            #pos_meta = (1, 2, 3, 8, 0, 4, 7, 6, 5, 0)

        super().__init__(pos_ini + (pos_ini.index(0),),
                         lambda pos: pos == pos_meta,
                         modelo8Puzzle())


def h_1(nodo):
    """
    Primer heurística para el 8-puzzle:
    Regresa el número de piezas mal colocadas.
    """
    return sum([1 for i in range(1, 9) if i != nodo.estado[i]])


def h_2(nodo):
    """
    Segunda heurística para el 8-puzzle:
    Regresa la suma de las distancias de manhattan
    de los numeros mal colocados.
    """
    return sum([abs(i % 3 - nodo.estado[i] % 3) +
                abs(i // 3 - nodo.estado[i] // 3)
                for i in range(9) if nodo.estado[i] != 0])

def solucion(pos_ini):
    
    print(modelo8Puzzle.dibuja(pos_ini))

    # ------- A* con h1 -----------
    print("---------- Utilizando A* con h1 -------------")
    problema = ochoPuzzle(pos_ini)
    solucion = busquedas.busqueda_A_estrella(problema, h_1)
    print(solucion)

    # ------- A* con h2 -----------
    #print("---------- Utilizando A* con h2 -------------")
    #problema = ochoPuzzle(pos_ini)
    #solucion = busquedas.busqueda_A_estrella(problema, h_2)
    #print(solucion)


if __name__ == "__main__":

    print("\nINICIANDO")
    #solucion((2, 8, 3, 1, 6, 4, 7, 0, 5))

    #solucion((5, 1, 3, 4, 0, 2, 6, 7, 8))

    solucion((7, 2, 4, 5, 0, 6, 8, 3, 1))