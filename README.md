# Srujan AI Chatbot

A modern, responsive AI chatbot web application powered by **Google Gemini (Gemma-3-1b-it)** and built with **Flask**.

![Chatbot UI](https://via.placeholder.com/800x400.png?text=Srujan+AI+Chatbot+Interface)

## 🚀 Features

- **Gemini Powered**: Uses the latest Gemma-3-1b-it model for intelligent and fast responses.
- **Glassmorphic UI**: Beautiful, modern interface with smooth gradients and animations.
- **Real-time Interaction**: Seamless chat experience with typing indicators.
- **Responsive Design**: Works perfectly on both desktop and mobile devices.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), JavaScript (Fetch API)
- **AI Engine**: Google Generative AI (Gemini SDK)

## 📋 Prerequisites

- Python 3.10 or higher
- A Google Gemini API Key. You can get one from the [Google AI Studio](https://aistudio.google.com/).

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ChatBot-master
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install flask google-generativeai
   ```

4. **Configure API Key**:
   Set your Google API Key as an environment variable:
   - **Windows (PowerShell)**: `$env:GOOGLE_API_KEY="your_api_key_here"`
   - **Linux/macOS**: `export GOOGLE_API_KEY="your_api_key_here"`
   
   *Alternatively, you can modify the `GOOGLE_API_KEY` default value in `app.py` (not recommended for production).*

## 🏃 Running the App

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 📄 License

This project is open-source. Feel free to use and modify it!

---
Developed by **Srujan**.
