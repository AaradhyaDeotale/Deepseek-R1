import requests

def generate_feedback(student_answer: str, correct_answer: str, error_type: str, notes: str) -> str:
    prompt = f"""
    **Task**: Explain the student's mistake and suggest study materials.
    Student Answer: {student_answer}
    Correct Answer: {correct_answer}
    Error Type: {error_type}
    Relevant Notes: {notes}
    """
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "deepseek-r1", "prompt": prompt, "stream": False}
    )
    return response.json().get("response", "Error generating feedback")