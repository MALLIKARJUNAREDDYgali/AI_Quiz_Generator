from pydantic import BaseModel

class QuizRequest(BaseModel):
    topic: str
    question_type: str  # "MCQ" or "Short Answer"
