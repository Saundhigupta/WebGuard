# 🛡️ WebGuard — ML-Based Web Application Firewall

A machine learning powered Web Application Firewall that detects 
and blocks SQL Injection and XSS attacks in real time.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![Accuracy](https://img.shields.io/badge/Accuracy-98.08%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Features

- Real time SQL Injection detection
- Real time XSS detection  
- ML model with 98.08% accuracy
- Confidence score on every prediction
- Live statistics dashboard
- Attack activity log
- Dual layer detection (Regex + ML)

## 🏗️ Architecture

User Input
    ↓
Flask Web App
    ↓
Layer 1: Regex Pattern Matching
    ↓
Layer 2: Naive Bayes ML Model
    ↓
Confidence Score
    ↓
BLOCK 🚨 or ALLOW ✅

## 🛠️ Tech Stack

- **Platform:** Kali Linux
- **Language:** Python 3
- **ML:** Scikit-learn (Naive Bayes)
- **Text Processing:** TF-IDF Vectorizer
- **Web Framework:** Flask
- **Frontend:** HTML, CSS, Jinja2

## 📊 Model Performance

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| NORMAL | 1.00 | 0.93 | 0.97 |
| SQL_INJECTION | 0.96 | 1.00 | 0.98 |
| XSS | 1.00 | 1.00 | 1.00 |
| **Overall** | **0.99** | **0.98** | **0.98** |

**Overall Accuracy: 98.08%**

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/webguard.git
cd webguard
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Generate the dataset
```bash
python build_research_dataset.py
```

4. Train the model
```bash
python train_model.py
```

5. Run the application
```bash
python app.py
```

6. Open browser and go to
```
http://localhost:5000
```

## 🧪 Testing

Try these payloads in the WebGuard interface:

**Normal inputs (should be ALLOWED):**
- `hello world`
- `john doe`
- `search query`

**SQL Injection (should be BLOCKED):**
- `1' OR '1'='1`
- `' UNION SELECT user, password FROM users -- -`
- `1; DROP TABLE users--`

**XSS (should be BLOCKED):**
- `<script>alert('XSS')</script>`
- `<img src=x onerror=alert(1)>`
- `<svg onload=alert(1)>`

## 📁 Project Structure

WebGuard/
├── app.py                    # Flask application
├── logger.py                 # Attack logger
├── train_model.py            # ML model training
├── create_dataset.py         # Dataset creation
├── expand_dataset.py         # Dataset expansion
├── build_research_dataset.py # Research grade dataset
├── requirements.txt          # Dependencies
├── data/
│   └── dataset.csv           # Training dataset
├── models/                   # Saved ML models
├── templates/
│   └── index.html            # Web interface
├── static/                   # CSS/JS files
└── logs/                     # Attack logs

## 🎓 Educational Purpose

This project was built for educational purposes as part of 
B.Tech Cybersecurity coursework. It demonstrates:

- Web attack simulation using DVWA
- Attack pattern capture and dataset creation
- Machine learning for security applications
- Real time threat detection and blocking

## ⚠️ Disclaimer

This project is for educational purposes only. 
Only test on systems you own or have permission to test.
The attack demonstrations were performed on DVWA — 
a deliberately vulnerable application designed for security training.

## 📚 References

- [OWASP Top 10](https://owasp.org/Top10)
- [DVWA](https://dvwa.co.uk)
- [Scikit-learn](https://scikit-learn.org)
- [Flask](https://flask.palletsprojects.com)
- [SecLists](https://github.com/danielmiessler/SecLists)
