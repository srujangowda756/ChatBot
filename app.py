from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import warnings

# Suppress the FutureWarning from google.generativeai
warnings.filterwarnings('ignore', category=FutureWarning)

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'AIzaSyB95QzTtqsVsv34Qhygua-R3x20ebfibH0')
genai.configure(api_key=GOOGLE_API_KEY)

# Use a smaller model to reduce cost / use a free tier if available
model = genai.GenerativeModel('models/gemma-3-1b-it')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400
            
        user_input = data.get('message', '').strip()
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        response_raw = chat.send_message(user_input)
        response_text = response_raw.text
        
        return jsonify({"response": response_text})
    
    except Exception as e:
        error_msg = str(e)
        print(f"Error: {error_msg}")
        return jsonify({"error": error_msg}), 500

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)
