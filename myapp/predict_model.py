# myapp/predict_model.py

def predict_iris_class(sepal_length, sepal_width, petal_length, petal_width):
    # This is just a dummy function for testing
    # Replace with your actual ML model logic later
    if float(petal_length) > 2:
        return "Iris-versicolor"
    else:
        return "Iris-setosa"
