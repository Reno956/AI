def vacuum():
    #Variables y estrucuturas utilizadas
    costo = 0
    solucion = ['']
    dicEstados = {'A': '0', 'B': '0','C':'0'}
    
    locacion = input("Ingrese la posicion inicial: ") #Ingreso de la posicion inicial 
    estado = input("Ingrese el estado de " + locacion + (" : ")) #Ingreso del estado de la posicon inicial
    #Ingreso de los demas estados
    if locacion == 'A':
        estadoB = input("Ingrese el estado de B: ")
        estadoC = input("Ingrese el estado de C: ")
        dicEstados['A'] = estado
        dicEstados['B'] = estadoB
        dicEstados['C'] = estadoC
    elif locacion == 'B':
        estadoC = input("Ingrese el estado de C: ")
        estadoB = input("Ingrese el estado de A: ")
        dicEstados['A'] = estadoB
        dicEstados['B'] = estado
        dicEstados['C'] = estadoC
    else:
        estadoC = input("Ingrese el estado de A: ")
        estadoB = input("Ingrese el estado de B: ")
        dicEstados['A'] = estadoC
        dicEstados['B'] = estadoB
        dicEstados['C'] = estado

    print("\nEstado Inicial")
    print(dicEstados)
    #Vacuum situado en A
    if locacion == 'A':        
        if estadoC == '1':
            print("\nEstado de C: Sucio")
            dicEstados['C'] = '0'
            costo += 3 
            solucion.append('RIGTH')
            solucion.append('RIGTH')
            solucion.append('SUCK')
            estadoC = 0
        else:
            print("\nEstado de C: Limpio")
            if estadoB == '1':
                print("Estado de B: Sucio")
                dicEstados['B'] = '0'
                costo += 2 
                solucion.append('RIGTH')
                solucion.append('SUCK')
                estadoB = 0
            else:
                if estado == '1':
                    print("Estado de A: Sucio")
                    dicEstados['A'] = '0'
                    costo += 1
                    solucion.append('SUCK') 
                    estado=0
        if estadoB == '1':
            print("Estado de B: Sucio")
            dicEstados['B'] = '0'
            costo += 2 
            solucion.append('LEFT')
            solucion.append('SUCK')
            estadoB = 0
        else:
            print("\nEstado de B: Limpio")
            if estado == '1':
                costo += 1 
                solucion.append('LEFT')
        if estado == '1':
            print("Estado de A: Sucio")
            dicEstados['A'] = '0'
            costo += 2
            solucion.append('LEFT')
            solucion.append('SUCK') 
        else:
            print("\nEstado de A: Limpio")
    #Vacuum situado en B
    elif locacion == 'B':
        if estadoC == '1':
            print("\nEstado de C: Sucio")
            dicEstados['C'] = '0'
            costo += 2 
            solucion.append('RIGTH')
            solucion.append('SUCK')
        else:
            print("\nEstado de C: Limpio")
            if estado == '1':
                print("Estado de B: Sucio")
                dicEstados['B'] = '0'
                costo += 1
                solucion.append('SUCK')
                estado = 0
        if estado == '1':
            print("Estado de B: Sucio")
            dicEstados['B'] = '0'
            costo += 2 
            solucion.append('LEFT')
            solucion.append('SUCK')
        else:
            print("\nEstado de B: Limpio")
            if estadoB == '1':
                costo += 1 
                solucion.append('LEFT')
        if estadoB == '1':
            print("Estado de A: Sucio")
            dicEstados['A'] = '0'
            costo += 2
            solucion.append('LEFT')
            solucion.append('SUCK') 
        else:
            print("\nEstado de A: Limpio")
    #Vacuum situado en C   
    else:
        if estado == '1':
            print("Estado de C: Sucio")
            solucion.append('SUCK')
            dicEstados['C'] = '0'
            costo += 1  
        else:
            print("\nEstado de C: Limpio")
        if estadoB == '1':
            print("Estado de B: Sucio")
            dicEstados['B'] = '0'
            costo += 2 
            solucion.append('LEFT')
            solucion.append('SUCK')
        else:
            print("\nEstado de B: Limpio")
            if estadoC == '1':
                costo += 1 
                solucion.append('LEFT')
        if estadoC == '1': 
            print("Estado de A: Sucio")
            dicEstados['A'] = '0'
            costo += 2 
            solucion.append('LEFT')
            solucion.append('SUCK')
        else:
            print("\nEstado de A: Limpio")

    solucion.remove('')
    return {'diccionario':dicEstados,'solucion':solucion,'costo':costo}


def main():
    resultados=vacuum()
    print("\nLimpieza terminada ")
    print(resultados['diccionario'])
    print("\nSolucion")
    print(resultados['solucion'])
    print("\nCosto: "+ str(resultados['costo']))

main()