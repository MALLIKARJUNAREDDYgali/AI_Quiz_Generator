Here you go — your **ready-to-copy README.md**:

---

```markdown
# 🧠 AI Quiz Generator

This is a Streamlit web app that uses an AI API to automatically generate quizzes on any topic.  
Users can choose the topic and question type (MCQ or Short Answer), answer the quiz interactively, and get scored with feedback.

---

## 📌 Features

- Enter any topic (e.g. Java, Photosynthesis, World History)
- Choose question type: Multiple-Choice (MCQ) or Short Answer
- AI generates 10 questions with answers and explanations
- Interactive quiz-taking experience
- Instant evaluation with score and feedback

---

## 📂 Project Structure

```

ai\_quiz/
│
├── backend/
│   └── utils.py         # Builds the prompt for the AI
│
├── app.py               # Main Streamlit app
├── .env                 # API keys and config
└── requirements.txt     # Project dependencies

````

---

## 🛠️ Technologies Used

- **Python** – core programming
- **Streamlit** – for building the web app
- **Requests** – for calling the AI API
- **python-dotenv** – to load secrets from .env

---

## ⚙️ How It Works

1. User enters a topic and selects question type (MCQ or Short Answer)
2. The app builds a prompt and sends it to the AI API
3. AI returns 10 questions with correct answers and explanations
4. The app displays the quiz interactively
5. User answers and submits the quiz
6. App evaluates answers and shows score + feedback

---

## 🚀 How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
````

### 2️⃣ Set up `.env` file

Create a `.env` file in the root folder with:

```
EURI_API_URL=https://your-api-url
EURI_API_KEY=your-api-key
EURI_MODEL=your-model-name
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## ✅ Example Usage

1. Open the app
2. Type "Java" as topic
3. Select "MCQ"
4. Click "Generate Quiz"
5. Answer all questions
6. Click "Submit"
7. See your score and feedback

---

## 🙌 Why This Project?

This project helps automate quiz creation for students and teachers.
It saves time and provides instant feedback for learning any topic.

---

## 📜 License

For educational and demo use. You are free to customize or build on it.

```

---

✅ Now you can paste this directly into your project as `README.md`.  
If you need this in `.txt`, `.docx`, or PDF format — I can export that too.
```
