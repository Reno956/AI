def recursive_dfs(graph, source,wrong,path = []):

    if source not in path:
        if source not in wrong:
            #Verifica que el elemento de entrada
            #no este dentro de la lista de erroneos
            path.append(source)
        if source not in graph:
            #Verifica que el elemento de entrada
            #este dentro del árbol
            return path

        for neighbour in graph[source]:
            #Metodo recursivo DFS
            path = recursive_dfs(graph, neighbour,wrong, path)
        
    return path

#Árbol de busqueda
graph = {"0000":["1000","1100", "1001","1010"],
           "1010":["0010"],
           "0010":["1011","1110"],
           "1011":["0011"],
           "1110":["0110","0100"],
           "0100":["1101"],
           "1101":["0001","0101"],
           "0001":["0111"],
           "0101":["1111"]}

#Lista de erroneos
wrong = ["1000","1100", "1001","0011","0110","0111"]

path = recursive_dfs(graph, "1000",wrong)

print(" ".join(path))