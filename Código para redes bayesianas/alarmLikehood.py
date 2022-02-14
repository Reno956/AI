from modelA import modelA

# Calculate probability for a given observation
probability = modelA.probability([["yes", "no", "no", "yes", "yes"]])

print(probability)
