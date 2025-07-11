# backend/backend.py

def generate_questions(topic):
    return [
        {
            "question": f"What is {topic}?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        },
        {
            "question": f"Why is {topic} important?",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 2"
        }
    ]
