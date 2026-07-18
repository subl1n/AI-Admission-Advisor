# AI Admission Advisor

AI Admission Advisor is a web application that helps students evaluate their chances of admission to universities using Artificial Intelligence.

Users can enter their academic profile, including GPA, IELTS, SAT scores, extracurricular activities, and target universities. The application sends this information to an AI model (DeepSeek) and generates a personalized admission analysis.

---

# Features

-  AI-powered admission analysis
-  Supports multiple universities in one request
-  Stores application history
-  View previous AI analyses
-  Modern web interface built with FastAPI and HTML
-  Local JSON database for storing applications

---

# Technologies

- Python
- FastAPI
- Jinja2
- HTML
- Bootstrap 5
- DeepSeek API
- JSON
- Git & GitHub

---

# Screens

- Home page with application form
- AI-generated admission analysis
- Application history
- Detailed analysis page
- About page

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Admission-Advisor.git
```

Open the project:

```bash
cd AI-Admission-Advisor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
DEEPSEEK_API_KEY=your_api_key
```

Run the server:

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

# Project Structure

```
AI-Admission-Advisor/
│
├── templates/
│   ├── index.html
│   ├── history.html
│   ├── result.html
│   ├── application.html
│   └── about.html
│
├── app.py
├── ai.py
├── database.py
├── db.json
├── .env
├── requirements.txt
└── README.md
```

---

# Note

The DeepSeek API key is stored locally in the `.env` file and is **not uploaded** to GitHub.

---

# Future Improvements

- User authentication
- PostgreSQL database
- PDF portfolio upload
- AI recommendations for improving admission chances
- University comparison
- Scholarship prediction
- Responsive mobile interface

---

# Author

**Aman**

High school student from Kyrgyzstan interested in Mechanical Engineering, Artificial Intelligence, and educational technology.

---

# License

This project is created for educational purposes.