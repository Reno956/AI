from modelR import model

pregunta=input("Ingrese el hecho a buscar: ")
evidencia=input("Dado que: ")
# Calculate predictions
predictions = model.predict_proba({
    f"{evidencia}": "yes"
})
#model.add_states(rain, sprinkles, neighbor, grass,dog)



# Print predictions for each node
#zip une el mismo elemento de las diferentes tuplas, si las tuplas son de diferente longitud
#la que tiene mas pierde sus elementos
for node, prediction in zip(model.states, predictions):
    #if predictiion es instance de string
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    elif node.name==pregunta:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            # precision en decimales, luego del punto 
            print(f"    {value}: {probability:.5f}")	
