import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

pickle_off = open("XGBoostClassifier.pkl", "rb")
emp = pickle.load(pickle_off)
print(emp)

app=Flask(__name__)
model =picke.load(open('XGBoostClassifier.pkl'),'rb')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='The URL is '.format(output))


if __name__ == "__main__":
    app.run(debug = True)

