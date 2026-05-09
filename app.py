from flask import Flask, render_template, request, redirect, session
import numpy as np
import joblib
from suggestion_engine import generate_suggestion

app = Flask(__name__)
app.secret_key = "water_secret"

# Load ML model
model = joblib.load("model.pkl")


# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        # Any username/password allowed
        session["user"] = username

        return redirect("/home")

    return render_template("login.html")


# ---------------- HOME ----------------
@app.route("/home")
def home():

    if "user" not in session:
        return redirect("/")

    return render_template("index.html")


# ---------------- PREDICT PAGE ----------------
@app.route("/predict")
def predict():

    if "user" not in session:
        return redirect("/")

    return render_template("predict.html")


# ---------------- WQI FUNCTION ----------------
def calculate_wqi(ph, do, bod, temp, turb):

    score = 0

    # pH
    if 6.5 <= ph <= 8.5:
        score += 20
    elif 6 <= ph <= 9:
        score += 12
    else:
        score += 5

    # DO
    if do >= 6:
        score += 20
    elif do >= 4:
        score += 12
    else:
        score += 5

    # BOD
    if bod <= 3:
        score += 20
    elif bod <= 6:
        score += 12
    else:
        score += 5

    # Temperature
    if temp <= 28:
        score += 20
    elif temp <= 32:
        score += 12
    else:
        score += 5

    # Turbidity
    if turb <= 5:
        score += 20
    elif turb <= 10:
        score += 12
    else:
        score += 5

    if score >= 80:
        quality = "GOOD"

    elif score >= 50:
        quality = "MODERATE"

    else:
        quality = "UNSAFE"

    return score, quality


# ---------------- RESULT ----------------
@app.route("/result", methods=["POST"])
def result():

    ph = float(request.form["ph"])
    do = float(request.form["do"])
    bod = float(request.form["bod"])
    temp = float(request.form["temp"])
    turb = float(request.form["turb"])

    # ML Prediction
    values = np.array([[ph, do, bod, temp, turb]])
    prediction = model.predict(values)[0]

    # WQI
    wqi, quality = calculate_wqi(
        ph,
        do,
        bod,
        temp,
        turb
    )

    suggestion = generate_suggestion(quality)

    return render_template(
        "result.html",
        result=quality,
        wqi=wqi,
        suggestion=suggestion,
        ph=ph,
        do=do,
        bod=bod,
        temp=temp,
        turb=turb
    )


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)