from modelM import model

# Calculate predictions
predictions = model.predict_proba({
    "metastasis": "yes",
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    #if predictiion es instance de string
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    elif node.name=="calcio":
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            # precision en decimales, luego del punto 
            print(f"    {value}: {probability:.5f}")	
