def vacuum():
    dicEstados = {'A': '0', 'B': '0'}
    costo = 0
    solucion = ['']

    locacion = input("Ingrese la posicion: ") 
    estado = input("Ingrese el estado de " + locacion + (" : ")) 
    estadoSiguiente = input("Ingrese el otro estado: ")

    if locacion == 'A':
        dicEstados['A'] = estado
        dicEstados['B'] = estadoSiguiente
    else: 
        dicEstados['B'] = estado
        dicEstados['A'] = estadoSiguiente

    print("Estado Inicial ")
    print(dicEstados)

    if locacion == 'A':        
        if estadoSiguiente == '1':
            dicEstados['B'] = '0'
            costo += 2 
            solucion.append('RIGTH')
            solucion.append('SUCK')
            estadoSiguiente = 0
        if estado == '1':
            dicEstados['A'] = '0'
            costo += 2
            solucion.append('LEFT')
            solucion.append('SUCK') 
    else:
        if estado == '1':
            solucion.append('SUCK')
            dicEstados['B'] = '0'
            costo += 1  
            if estadoSiguiente == '1':
                dicEstados['A'] = '0'
                costo += 2 
                solucion.append('LEFT')
                solucion.append('SUCK')
        else:
            if estadoSiguiente == '1': 
                dicEstados['A'] = '0'
                costo += 2 
                solucion.append('LEFT')
                solucion.append('SUCK')
    solucion.remove('')
    print("Limpieza terminada ")
    print(dicEstados)
    print("Solucion")
    print(solucion)
    print("Costo: " + str(costo))

vacuum()