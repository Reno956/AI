import heapq

class problemaBusqueda:
    
    def __init__(self, x0, meta, modelo):
        """
        Inicializa el problema de búsqueda
        x0: Una tupla con un estado válido del problema (estado inicial).
        meta: Una función meta(s) --> bool,
                     donde meta(s) devuelve True solo
                     si el estado s es un estado objetivo.
        """
        def es_meta(estado):
            self.num_nodos += 1
            return meta(estado)
        self.es_meta = es_meta

        self.x0 = x0
        self.modelo = modelo
        self.num_nodos = 0  


class Nodo:
    def __init__(self, estado, accion=None, padre=None, costo_local=0):
        """
        Inicializa un nodo como una estructura
        """
        self.estado = estado
        self.accion = accion
        self.padre = padre
        self.costo = 0 if not padre else padre.costo + costo_local
        self.profundidad = 0 if not padre else padre.profundidad + 1
        self.nodos_visitados = 0

    def expande(self, modelo):
       
        return (
            Nodo(
                modelo.sucesor(self.estado, a),
                a,
                self,
                modelo.costo_local(self.estado, a))
            for a in modelo.acciones_legales(self.estado))

    def genera_plan(self):
        
        return ([self.estado] if not self.padre else
                self.padre.genera_plan() + [self.accion, self.estado])

    def __str__(self):
        """
        Muestra el nodo como un plan.
        """
        plan = self.genera_plan()
        return ("Costo: {}\n".format(self.costo) +
                "Solucion:\n\n" +
                "".join(["Estado    {} \nMovimiento {} \nResultado {}\n\n".format(x, a, xp)
                         for (x, a, xp)
                         in zip(plan[:-1:2], plan[1::2], plan[2::2])]))

    def __lt__(self, other):
        return self.profundidad < other.profundidad

def busqueda_A_estrella(problema, heuristica):
    frontera = []
    heapq.heappush(frontera, (0, Nodo(problema.x0)))
    visitados = {problema.x0: 0}
    
    while frontera:
        (_, nodo) = heapq.heappop(frontera)
        if problema.es_meta(nodo.estado):
            nodo.nodos_visitados = problema.num_nodos
            return nodo
        for hijo in nodo.expande(problema.modelo):
            if hijo.estado not in visitados or visitados[hijo.estado] > hijo.costo :
                heapq.heappush(frontera, (hijo.costo + heuristica(hijo), hijo))
                visitados[hijo.estado] = hijo.costo
    return None

class modeloBusqueda:
    
    def acciones_legales(self, estado):
        raise NotImplementedError("No implementado todavía.")

    def sucesor(self, estado, accion):
        raise NotImplementedError("No implementado todavía.")

    def costo_local(self, estado, accion):
        return 1    