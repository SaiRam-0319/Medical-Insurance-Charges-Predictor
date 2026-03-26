# 🏥 Medical Insurance Charges Predictor

A Machine Learning web application that predicts medical insurance charges
based on personal attributes like age, BMI, smoking status, and region.

---

## 📌 Project Overview

| Detail | Info |
|--------|------|
| **Problem Type** | Supervised Learning → Regression |
| **Target Variable** | `charges` (Medical Insurance Cost in USD) |
| **Dataset** | insurance.csv (1338 rows × 7 columns) |
| **Best Model** | Random Forest Regressor |
| **Deployment** | Streamlit Cloud |

---

## 📊 Dataset Features

| Feature | Type | Description |
|---------|------|-------------|
| `age` | Numerical | Age of the policyholder |
| `sex` | Categorical | Gender (male / female) |
| `bmi` | Numerical | Body Mass Index |
| `children` | Numerical | Number of dependents |
| `smoker` | Categorical | Smoking status (yes / no) |
| `region` | Categorical | Residential region in US |
| `charges` | **Target** | Medical insurance cost (USD) |

---

## 🤖 Algorithms Used

| Algorithm | R² Score | RMSE | MAE |
|-----------|----------|------|-----|
| Linear Regression | 0.8047 | 0.4189 | 0.2697 |
| Ridge Regression | 0.8047 | 0.4190 | 0.2698 |
| **Random Forest** | **0.8483** | **0.3693** | **0.1948** |

✅ **Random Forest** is the best performing model.

---

## 📁 Project Structure

```
📂 Project Folder
   ├── app.py                        ← Streamlit Web App
   ├── requirements.txt              ← Dependencies
   ├── model.pkl                     ← Saved Random Forest Model
   ├── scaler.pkl                    ← Saved Standard Scaler
   ├── insurance.csv                 ← Dataset
   └── Medical_Insurance_Cost_ML.ipynb ← Jupyter Notebook
```

---

## 🔧 Steps Performed

```
✅ 1. Understand Business Problem
✅ 2. Load Dataset
✅ 3. EDA (Exploratory Data Analysis)
✅ 4. Statistical Analysis (Skewness & Kurtosis)
✅ 5. Visualization (Histplot, Boxplot, Heatmap, Pairplot)
✅ 6. Feature Engineering (Encoding, Log Transform, Scaling)
✅ 7. Model Building (Linear, Ridge, Random Forest)
✅ 8. Model Evaluation (R², RMSE, MAE)
✅ 9. Deployment (Streamlit)
```

---

## ⚙️ How to Run Locally

**Step 1 — Clone the Repository**
```
git clone https://github.com/yourusername/insurance-predictor.git
cd insurance-predictor
```

**Step 2 — Install Dependencies**
```
pip install -r requirements.txt
```

**Step 3 — Run the App**
```
streamlit run app.py
```

**Step 4 — Open in Browser**
```
http://localhost:8501
```

---

## 🌐 Live Demo

👉 [Click here to open the app](https://yourapp.streamlit.app)

---

## 📦 Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Plotting |
| `seaborn` | Statistical visualization |
| `scikit-learn` | Machine learning models |
| `streamlit` | Web app deployment |
| `scipy` | Statistical analysis |
| `pickle` | Save & load model |

---

## 📈 Key Findings

- 🚬 **Smoker** is the strongest predictor of charges (correlation ≈ 0.79)
- 📅 **Age** has moderate positive correlation with charges
- ⚖️ **BMI** has moderate positive correlation, stronger in smokers
- 🗺️ **Region** has minimal impact on charges
- 💡 **Log Transform** applied on `charges` to reduce skewness

---

## 👨‍💻 Author

**Your Name**
- GitHub  : github.com/yourusername
- Email   : youremail@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
