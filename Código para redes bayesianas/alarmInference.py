from modelA import modelA

# Calculate predictions
predictions = modelA.predict_proba({ 
    "terremoto": "yes"
    #"jhon": "yes",
    #"maria": "yes"
})

# Print predictions for each node
for node, prediction in zip(modelA.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    elif node.name=="robo":
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.5f}")

