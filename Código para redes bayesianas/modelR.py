from pomegranate import *

rain=Node(DiscreteDistribution({ "yes":0.2,
    "no":0.8,
}), name="rain")

sprinkles=Node(DiscreteDistribution({
    "yes":0.6, 
    "no":0.4,
}), name="sprinkles")

neighbor = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", 0.3],
    ["yes", "no", 0.7], 
    ["no", "yes", 0.4], 
    ["no", "no", 0.6],
], [rain.distribution]), name="neighbor")

grass = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", "yes", 0.9],
    ["yes", "yes", "no", 0.1], 
    ["yes", "no", "yes", 0.7], 
    ["yes", "no", "no", 0.3], 
    ["no", "yes", "yes", 0.8], 
    ["no", "yes", "no", 0.2], 
    ["no", "no", "yes", 0.2], 
    ["no", "no", "no", 0.8],
], [rain.distribution,sprinkles.distribution]), name="grass")

dog = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", "yes", 0.9],
    ["yes", "yes", "no", 0.1],
    ["yes", "no", "yes", 0.4], 
    ["yes", "no", "no", 0.6], 
    ["no", "yes", "yes", 0.5], 
    ["no", "yes", "no", 0.5], 
    ["no", "no", "yes", 0.3], 
    ["no", "no", "no", 0.7],
], [neighbor.distribution,grass.distribution]), name="dog")

model = BayesianNetwork()
model.add_states(rain, sprinkles, neighbor, grass,dog)

# # conecto las flechas de los nodos
model.add_edge(rain, neighbor) 
model.add_edge(rain, grass) 
model.add_edge(sprinkles, grass) 
model.add_edge(neighbor,dog) 
model.add_edge(grass,dog)

# Finalize model, model.bake genera el modelo. 
model.bake()	
		
