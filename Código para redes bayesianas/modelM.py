from pomegranate import *

metastasis = Node(DiscreteDistribution({ 
    "yes": 0.2,
    "no":0.8
}), name="metastasis")

# Train node is conditional on rain and maintenance 

tumor = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", 0.2],
    ["no", "yes", 0.05], 
    ["yes", "no", 0.8], 
    ["no", "no", 0.95]
], [metastasis.distribution]), name="tumor")

calcio = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", 0.8],
    ["no", "yes", 0.2], 
    ["yes", "no", 0.2], 
    ["no", "no", 0.8]
], [metastasis.distribution]), name="calcio")

coma = Node(ConditionalProbabilityTable([
    ["yes", "yes", "yes", 0.8], 
    ["yes", "no", "yes", 0.7], 
    ["no", "yes", "yes", 0.9], 
    ["no", "no", "yes", 0.05], 
    ["yes", "yes", "no", 0.2], 
    ["yes", "no", "no", 0.3], 
    ["no", "yes", "no", 0.3], 
    ["no", "no", "no", 0.95],
], [tumor.distribution, calcio.distribution]), name="coma")

jaqueca = Node(ConditionalProbabilityTable([ 
    ["yes", "yes", 0.6],
    ["no", "yes", 0.2], 
    ["yes", "no", 0.4], 
    ["no", "no", 0.8]
], [tumor.distribution]), name="jaqueca")

#creo una red bayesana y agrego los estados 
model = BayesianNetwork()
model.add_states(metastasis,tumor,calcio,coma,jaqueca)

# conecto las flechas de los nodos 
model.add_edge(metastasis,tumor) 
model.add_edge(metastasis,calcio) 
model.add_edge(tumor,coma) 
model.add_edge(calcio,coma)
model.add_edge(tumor,jaqueca) 

model.bake()
