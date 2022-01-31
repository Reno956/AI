class Node:
    def __init__(self, llave):
        self.dato = llave
        self.izq = None
        self.der = None
 
def printLevelOrder(raiz):
    if raiz is None:
        return
 
    queue = []
    salida = []
 
    queue.append(raiz)
 
    while(len(queue) > 0):
 
        salida.append(queue[0].dato)
        nodo = queue.pop(0)

        if nodo.izq is not None:
            queue.append(nodo.izq)
 
        if nodo.der is not None:
            queue.append(nodo.der)
    print(salida)
 
raiz = Node(0)
raiz.izq = Node(1)
raiz.izq = Node(2)
raiz.izq = Node(3)
raiz.der = Node(4)
raiz.der.izq = Node(5)
raiz.der.izq.izq = Node(6)
raiz.der.izq.izq.izq = Node(8)
raiz.der.izq.der = Node(7)
raiz.der.izq.der.izq = Node(9)
raiz.der.izq.der.der = Node(10)
raiz.der.izq.der.der.der = Node(11)
raiz.der.izq.der.der.der.izq = Node(12)
raiz.der.izq.der.der.der.izq.izq = Node(14)
raiz.der.izq.der.der.der.der = Node(13)
raiz.der.izq.der.der.der.der.der = Node(15)
 
print("\nSolucion\n")
printLevelOrder(raiz)