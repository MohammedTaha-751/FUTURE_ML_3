# FUTURE_ML_3 - Customer Support Chatbot 💬

This is my beginner-level chatbot project built as part of my internship at **FUTURE INTERNS**.  
It uses Python, Flask, and basic NLP (TF-IDF + Cosine Similarity) to answer customer queries based on a FAQ file.

---

## 🔧 Features

- 📚 Answers questions using similarity matching  
- 🧠 Built with TF-IDF + Cosine Similarity  
- 🌐 Simple Flask web interface  
- 🛠️ REST API for chat and insights  
- 📊 Easily customizable FAQ dataset  

---

## 🚀 How to Run

Step-by-step:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set the FAQ path (Windows):
   ```bash
   set FAQ_PATH=data/faq.json
   ```

   Or (Linux/macOS):
   ```bash
   export FAQ_PATH=data/faq.json
   ```

3. Run the app:
   ```bash
   python web/app.py
   ```

Then open your browser and go to:  
**http://localhost:5000**

---

## 🧪 Run Tests

```bash
python -m unittest tests/test_chatbot.py
```

---

## 📁 Project Structure

```
FUTURE_ML_3/
├── chatbot/           # Chatbot logic (NLP model)
├── data/              # FAQ data (faq.json)
├── tests/             # Unit tests
├── web/               # Flask app
│   └── templates/     # HTML interface
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## ✍️ Customizing FAQs

To change the questions and answers, edit the file:

```
data/faq.json
```

Use this format:

```json
{
  "faqs": [
    {
      "question": "Your question here?",
      "answer": "Answer goes here."
    }
  ]
}
```

---

## 📢 Intern Note

This project was created during my internship at **FUTURE INTERNS**  
as part of the `FUTURE_ML_3` learning module. I learned about NLP, Flask, and building simple AI apps.

---

## 🌐 Author

**Mohammed Taha Ahamed**  
LinkedIn: [www.linkedin.com/in/mohammed-taha-ahamed-02bb26335]  
GitHub: [https://github.com/MohammedTaha-751]
