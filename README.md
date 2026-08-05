# 📧 Gmail Spam Detection using Machine Learning

A web-based **Email Spam Detection** application that uses **Machine Learning** and **Natural Language Processing (NLP)** to classify email messages as **Spam** or **Not Spam (Ham)**. The application provides an intuitive interface where users can enter email text and receive instant predictions.

---

## 🚀 Features

* Detects whether an email is **Spam** or **Not Spam**
* Interactive and responsive web interface
* Machine Learning-powered classification
* NLP-based text preprocessing
* Fast real-time predictions
* Easy to run locally using Flask

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **NLTK**
* **Pickle**
* **HTML**
* **CSS**

---

## 📂 Project Structure

```
gmail-spam-detection/
│
├── static/                # CSS, images, and other static files
├── templates/             # HTML templates
├── app.py                 # Flask application
├── model.pkl              # Trained machine learning model
├── vectorizer.pkl         # TF-IDF Vectorizer
├── requirements.txt       # Project dependencies
├── spam.csv               # Dataset
├── README.md
└── .gitignore
```

---

## 🧠 How It Works

1. The user enters an email message.
2. The text is cleaned and preprocessed.
3. The TF-IDF Vectorizer converts the text into numerical features.
4. The trained Machine Learning model predicts whether the message is spam.
5. The prediction is displayed instantly on the webpage.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/ashaangadi18/gmail-spam-detection.git
```

### Navigate to the project folder

```bash
cd gmail-spam-detection
```

### Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📊 Machine Learning Pipeline

* Data Collection
* Text Cleaning
* Tokenization
* Stopword Removal
* Stemming/Lemmatization
* TF-IDF Vectorization
* Model Training
* Spam Prediction

---

## 📸 Output

The application classifies the entered email as:

* ✅ **Not Spam**
* 🚫 **Spam**

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Common libraries include:

* Flask
* scikit-learn
* pandas
* numpy
* nltk

---

## 🌱 Future Enhancements

* Gmail API integration
* Deep Learning models (LSTM/BERT)
* Spam probability score
* Email attachment scanning
* User authentication
* Dashboard with prediction history

---

## 🤝 Contributing

Contributions are welcome.

1. Fork this repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Asha Angadi**

GitHub: https://github.com/ashaangadi18

---

⭐ If you found this project useful, consider giving the repository a star.
