# 🎓 Placement Predictor

A Machine Learning based Placement Predictor built using **Python, Flask, Scikit-Learn, HTML, and CSS**.

The application predicts a student's placement chances based on:

* CGPA
* Aptitude Score
* Number of Projects

It also provides:

* Placement Probability (%)
* Personalized Recommendations
* Modern Dashboard UI

---

## 🚀 Features

### 📊 Placement Prediction

Predicts whether a student has a high or low chance of getting placed using a Random Forest Machine Learning model.

### 📈 Placement Probability

Displays the placement probability percentage.

Example:

* High Placement Chance ✅ (92%)
* Low Placement Chance ❌ (18%)

### 💡 Personalized Recommendations

Provides suggestions based on the student's profile.

Examples:

* Improve CGPA
* Improve Aptitude Score
* Build More Projects
* Participate in Hackathons
* Create a Portfolio Website

### 🎨 Modern Dashboard UI

* Responsive Design
* Progress Bar
* Professional Card Layout
* Reset Functionality

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3

### Backend

* Flask

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* Pandas
* NumPy

### Model Persistence

* Pickle (.pkl)

---

## 📂 Project Structure

```text
Placement_Predictor
│
├── app.py
├── train_model.py
├── dataset.csv
├── model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── static
│   └── style.css
│
└── templates
    └── index.html
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/venmugilrajan/Placement_prediction.git
```

### Move into Project Directory

```bash
cd Placement_prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

### Dataset

The model is trained using:

* CGPA
* Aptitude Score
* Projects

Target:

* Placed (1)
* Not Placed (0)

### Train-Test Split

```python
test_size = 0.2
random_state = 42
```

### Model

```python
RandomForestClassifier()
```

### Accuracy Evaluation

The model is evaluated using:

```python
accuracy_score()
```

### Model Saving

```python
pickle.dump()
```

Saved as:

```text
model.pkl
```

---

## 📊 Example Input

| CGPA | Aptitude | Projects |
| ---- | -------- | -------- |
| 8.5  | 80       | 4        |

### Output

```text
High Placement Chance ✅
Placement Probability: 92%
```

### Recommendations

```text
✓ Continue skill development
✓ Participate in hackathons
✓ Create a portfolio website
```

---

## 🔮 Future Enhancements

* Aptitude Test Module
* User Authentication
* Placement History Tracking
* Database Integration (SQLite/MySQL)
* Dark Mode
* Resume Analyzer
* Interview Readiness Assessment
* Online Deployment

---

## 👨‍💻 Author

**Venmugil Rajan S**

Passionate about:

* Full Stack Development
* Machine Learning
* UI/UX Design
* Problem Solving

GitHub:
https://github.com/venmugilrajan

---

## 📜 License

This project is licensed under the MIT License.
