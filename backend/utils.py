def generate_prompt(topic: str, qtype: str) -> str:
    if qtype.upper() == "MCQ":
        return f"""
You are an expert question generator. Create exactly 10 multiple-choice questions for the topic: "{topic}".

Each item must include:
- "question": the MCQ question text
- "options": list of 4 choices
- "answer": correct answer text
- "explanation": short explanation

Return the result as a valid JSON array of 10 objects using this format:
[
  {{
    "question": "...",
    "options": ["...", "...", "...", "..."],
    "answer": "...",
    "explanation": "..."
  }},
  ...
]
Only return the JSON — no extra text or instructions.
"""
    else:
        return f"""
You are an expert tutor. Create exactly 10 short-answer questions for the topic: "{topic}".

Each item must include:
- "question": the short-answer question text
- "answer": correct answer
- "explanation": short explanation

Return the result as a valid JSON array of 10 objects like:
[
  {{
    "question": "...",
    "answer": "...",
    "explanation": "..."
  }},
  ...
]
Only return the JSON — no extra text or comments.
"""
