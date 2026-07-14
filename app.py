from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model once at the start
model = pickle.load(open('diabetes.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data (strip any extra spaces from names)
            Pregnancies = int(request.form['Pregnancies'])
            Glucose = int(request.form['Glucose'])
            Bloodpressure = int(request.form['Bloodpressure'])
            BMI = float(request.form['BMI'])
            Age = int(request.form['Age'])

            # Combine inputs into one data row
            data = [[Pregnancies, Glucose, Bloodpressure, BMI, Age]]

            # Make prediction
            prediction = model.predict(data)[0]
            result = "Positive for Diabetes" if prediction == 1 else "Negative for Diabetes"

            return render_template('index.html', prediction=result)

        except Exception as e:
            return f"Error occurred: {e}"






























































if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
