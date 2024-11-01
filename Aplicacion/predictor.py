def make_prediction(model):
    prediction = model.forecast(steps=1)
	
    return prediction[0]