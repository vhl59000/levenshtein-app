# 🔤 Levenshtein Streamlit App

## 📌 Overview
This project was built as part of the assignment:

> *"Take any of the data science projects you have completed last year (or a personal one), make it as a Streamlit app and then containerize that app. Of course everything should be properly documented in a Git project, with tests on your data importing / filtering functions and the associated CI process."*

To satisfy the requirements, the repo has **two parts**:

### 1. Streamlit App (Levenshtein distance)
- User inputs two words.  
- The app computes the **Levenshtein distance** and a **normalized similarity score**.  
- Thought it would be funny to build this levenshtein distance computing app.

### 2. Data Import & Filtering Module
- Afterwards, I noticed that I should have an "import/filter data + unit tests" (in the guidelines.) so:
- A small dataset (`words.csv`) is included.  
- Functions allow **loading words** and **filtering them by length**.  
 

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ (tested on 3.11)  
- (Optional) Docker  
- (Optional) Virtual environment (`venv`, `conda`, etc.)  

### 1) Clone the repository
```bash
git clone https://github.com/vhl59000/levenshtein-app
cd levenshtein-app
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the Streamlit app
```bash
streamlit run app.py
```
App runs on 👉 [http://localhost:8501](http://localhost:8501)

### 4) Run tests
```bash
pytest -q
```

✅ Tests cover:
- Levenshtein distance logic  
- Data import (`load_words`) and filtering (`filter_words`)  

### 5) Run with Docker (optional)
```bash
docker build -t levenshtein-app .
docker run --rm -p 8501:8501 levenshtein-app
```

App available at 👉 [http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure
```
levenshtein-app/
│
├── app.py                 # Streamlit app
├── requirements.txt       # Dependencies
├── Dockerfile             # Containerization
├── words.csv              # Sample dataset
│
├── src/                   # Source code
│   ├── levenshtein.py     # Levenshtein distance function
│   └── data_io.py         # Data import & filter functions
│
├── tests/                 # Unit tests
│   ├── test_levenshtein.py
│   └── test_data_io.py
│
└── .gitlab-ci.yml         # CI pipeline (runs pytest)
```

---

## ✅ Deliverables
- GitLab repository with:
  - Streamlit app  
  - Unit tests  
  - GitLab CI (pytest)  
  - Dockerfile for containerization  
