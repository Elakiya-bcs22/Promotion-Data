# 📈 Promotion Data Predictor — Logistic Regression (Flask App)

A compact end-to-end ML project that predicts employee promotion likelihood using **Logistic Regression**, wrapped nicely in a **Flask** web interface.

---

## 🔎 Overview
This project trains a logistic regression model to estimate whether an employee may be promoted based on features like performance ratings and years of experience. The trained model is integrated into a web app for easy predictions.

---

## ✨ Features
- 🧩 Clean training & prediction pipeline (`train.py`, `app.py`)  
- 💾 Persists the model and scaler using `pickle`  
- 🌐 User-friendly Flask interface with templates  
- ⚡ Easily extendable for RESTful predictions  

---

## 📂 Project Structure
```
Promotion-Data/
├─ app.py                  # Flask application for UI/API
├─ train.py                # Model training logic
├─ employee_promotion_data.csv   # Dataset
├─ model.pkl               # Saved logistic regression model
├─ scaler.pkl              # Saved scaler for preprocessing
├─ requirements.txt        # Python dependencies
└─ templates/
   └─ index.html           # Web form for inputs & predictions
```

---

## 🛠 Tech Stack
- 🐍 **Python**, **Flask**  
- 📊 **pandas**, **numpy**, **scikit-learn**  
- 🎨 **Jinja2** for HTML templating  

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.8+ installed  
- `pip` (virtual environment recommended)

### ⚙️ Installation
```bash
git clone https://github.com/Elakiya-bcs22/Promotion-Data.git
cd Promotion-Data

# (Recommended) Create & activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

---

### 🏋️ Train the Model
Ensure `employee_promotion_data.csv` is in place with relevant feature columns. Then:
```bash
python train.py
```
This generates `model.pkl` and `scaler.pkl`.

---

### ▶️ Run the App
```bash
python app.py
```
Visit 👉 `http://127.0.0.1:5000/` to interact with the app.

---

## 📊 Dataset
- File: `employee_promotion_data.csv`  
- Example features: `experience_years`, `performance_score`, `last_promotion_years_ago`, etc. (adjust as needed)

---

## 🧠 Modeling Approach
- **Model**: `LogisticRegression` from scikit-learn  
- **Preprocessing**: Scaling numerical features for consistency  
- **Artifacts**:
  - `model.pkl`: Trained prediction model  
  - `scaler.pkl`: Corresponding scaler for new data inputs  

---

## 🔌 API (Optional)
You can extend `app.py` to support a JSON-based REST endpoint:

**Endpoint**: `POST /predict`

**Request (example)**:
```json
{
  "features": {
    "experience_years": 5,
    "performance_score": 4.2,
    "last_promotion_years_ago": 2
  }
}
```

**Response**:
```json
{
  "promotion_probability": 0.78
}
```

---

## 📈 Evaluation Metrics
Record and log metrics like:
- 🎯 Accuracy  
- 📐 Precision, Recall, F1 Score  
- 📊 ROC AUC for performance analysis  

Example output:
```
Accuracy: 0.85  
Precision: 0.80  
Recall: 0.75  
F1 Score: 0.77  
ROC AUC: 0.88
```

---

## 🖼 Results & Screenshots
Include a screenshot of your app’s UI here:
```html
<img src="assets/ui_preview.png" alt="App UI Preview" width="600"/>
```
_Example image—replace with actual screenshot!_

Insights:  
- Employees with higher performance scores have noticeably higher promotion probabilities.  
- Longer time since last promotion correlates with lower chances—unless balanced by stellar recent performance.  

---

## 🛠 Troubleshooting
- ❌ Missing dependencies? → `pip install -r requirements.txt`  
- ❌ Pickle files not found? → Run `python train.py` first  
- ❌ UI not displaying? → Ensure `app.py` and `templates/index.html` are properly set up  
- ❌ Port conflicts? → Change in `app.run(port=####)`  

---

## 🗺 Roadmap
- [ ] 📊 Add feature importance visuals  
- [ ] 📈 Integrate interactive charts & data EDA  
- [ ] 🐳 Add Docker support  
- [ ] 📡 Log user predictions for feedback loop  
- [ ] ☁️ Deploy the app online (Heroku, AWS, GCP)  

---

## 🤝 Contributing
Contributions are welcome! Please open issues or submit pull requests to discuss updates.

---

## 📄 License
Licensed under MIT License (default). Update if you’re using a different license.

---

## 🙌 Acknowledgements
- Thanks to the **scikit-learn** and **Flask** communities  
- Shout-out to any datasets or references that inspired this project  

