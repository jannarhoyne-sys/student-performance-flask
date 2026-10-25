from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


# Home page: show the form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    math_score = float(request.form['math_score'])
    reading_score = float(request.form['reading_score'])
    writing_score = float(request.form['writing_score'])

    # Same order as training: math, reading, writing
    features = [[math_score, reading_score, writing_score]]

    # The pipeline scales the input itself, then predicts
    prediction = model.predict(features)[0]

    # Probability for every group, as percentages, highest first
    probs = model.predict_proba(features)[0]
    probabilities = [(group, round(p * 100, 1)) for group, p in zip(model.classes_, probs)]
    probabilities.sort(key=lambda item: item[1], reverse=True)

    return render_template('index.html', predict=prediction, probabilities=probabilities)


if __name__ == '__main__':
    app.run(debug=True)