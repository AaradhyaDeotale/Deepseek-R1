from flask import Flask, request, jsonify
from flask_cors import CORS
import requests          
import os
from dotenv import load_dotenv
import logging
load_dotenv()  # Load environment variables

app = Flask(__name__)
CORS(app)  # Enable CORS

# Ollama configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
app.logger.setLevel(logging.DEBUG)

@app.route('/api/upload-notes', methods=['POST'])
def upload_notes():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400
    
    # Use absolute path
    upload_dir = os.path.abspath('uploads')
    os.makedirs(upload_dir, exist_ok=True)
    file.save(os.path.join(upload_dir, file.filename))

    return jsonify({"status": "Notes uploaded", "filename": file.filename})

@app.route('/api/generate-feedback', methods=['POST'])
def generate_feedback():
    data = request.json
    prompt = f"""
    Student Answer: {data['student_answer']}
    Correct Answer: {data['correct_answer']}
    Error Type: {data['error_type']}
    Notes: {data['relevant_notes']}
    Provide feedback and recommendations:
    """
    
    response = requests.post(
        OLLAMA_ENDPOINT,
        json={"model": "deepseek-r1", "prompt": prompt, "stream": False}
    )
    
    return jsonify({"feedback": response.json()["response"]})

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(port=5000, debug=True)
    
@app.errorhandler(500)
def handle_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def handle_not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404