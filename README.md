# Water Quality Prediction System

A Flask-based AI project that predicts water quality using Machine Learning.

---

## Features

- Login System
- Water Quality Prediction
- Water Quality Index (WQI)
- SAFE / MODERATE / UNSAFE Detection
- Graph Visualization
- Suggestion System

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Chart.js
- Scikit-learn

---

## Water Parameters

- pH
- Dissolved Oxygen (DO)
- Biological Oxygen Demand (BOD)
- Temperature
- Turbidity

---

## Water Quality Index (WQI)

| WQI Score | Status |
|---|---|
| 80 - 100 | SAFE |
| 50 - 79 | MODERATE |
| Below 50 | UNSAFE |

---

## Safe Ranges

| Parameter | Safe Range |
|---|---|
| pH | 6.5 - 8.5 |
| DO | >= 6 |
| BOD | <= 3 |
| Temperature | <= 28°C |
| Turbidity | <= 5 |

---

## Run Project

```bash
python train_model.py
python app.py

web link:
https://water-quality-prediction-0028.onrender.com
