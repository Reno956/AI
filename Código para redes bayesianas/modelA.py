from pomegranate import *

robo = Node(DiscreteDistribution({ 
    "yes": 0.001,
    "no":0.999
}), name="robo")

terremoto = Node(DiscreteDistribution({
    "yes": 0.002, 
    "no":0.998
}), name="terremoto")

# El nodo mantenimiento esta condicionado por la lluvia
# node condicional es una tabla con dos columnas, la primera columna tiene todas las probabilidades

# Train node is conditional on rain and maintenance 
alarma = Node(ConditionalProbabilityTable([
    ["yes", "yes", "yes", 0.95], 
    ["yes", "no", "yes", 0.94], 
    ["no", "yes", "yes", 0.29], 
    ["no", "no", "yes", 0.001], 
    ["yes", "yes", "no", 0.05], 
    ["yes", "no", "no", 0.06], 
    ["no", "yes", "no", 0.71], 
    ["no", "no", "no", 0.999],
], [robo.distribution, terremoto.distribution]), name="alarma")

jhon = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", 0.9],
    ["no", "yes", 0.05], 
    ["yes", "no", 0.1], 
    ["no", "no", 0.95]
], [alarma.distribution]), name="jhon")

maria = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", 0.70],
    ["no", "yes", 0.01], 
    ["yes", "no", 0.30], 
    ["no", "no", 0.99]
], [alarma.distribution]), name="maria")

#creo una red bayesana y agrego los estados 
modelA = BayesianNetwork()
modelA.add_states(robo, terremoto, alarma, jhon,maria)

# conecto las flechas de los nodos 
modelA.add_edge(robo, alarma) 
modelA.add_edge(terremoto, alarma) 
modelA.add_edge(alarma,jhon) 
modelA.add_edge(alarma,maria)

modelA.bake()
