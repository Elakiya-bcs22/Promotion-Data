from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Collect form inputs
    features = [float(x) for x in request.form.values()]
    final_features = scaler.transform([features])
    
    # Predict
    prediction = model.predict(final_features)[0]
    result = "Employee will be Promoted ✅" if prediction == 1 else "Employee will NOT be Promoted ❌"
    
    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
