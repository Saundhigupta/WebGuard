from flask import Flask, render_template, request
import pickle
import json
from datetime import datetime

app = Flask(__name__)

# Load the trained model and vectorizer
with open("models/webguard_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict(input_string):
    vec = vectorizer.transform([input_string])
    prediction = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)[0]
    confidence = round(max(probabilities) * 100, 2)
    return prediction, confidence

def get_logs():
    logs = []
    try:
        with open("logs/requests.log", "r") as f:
            lines = f.readlines()
            for line in reversed(lines[-10:]):
                logs.append(json.loads(line.strip()))
    except:
        pass
    return logs

def get_stats():
    stats = {"total": 0, "blocked": 0, "allowed": 0}
    try:
        with open("logs/requests.log", "r") as f:
            for line in f:
                entry = json.loads(line.strip())
                stats["total"] += 1
                if entry["attack_type"] != "NORMAL":
                    stats["blocked"] += 1
                else:
                    stats["allowed"] += 1
    except:
        pass
    return stats

def save_log(input_string, attack_type):
    log_entry = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "input": input_string,
        "attack_type": attack_type
    }
    with open("logs/requests.log", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    user_input = None

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            result, confidence = predict(user_input)
            save_log(user_input, result)

    logs = get_logs()
    stats = get_stats()

    return render_template("index.html",
                     result=result,
                     confidence=confidence if result else None,
                     user_input=user_input,
                     logs=logs,
                     stats=stats)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)