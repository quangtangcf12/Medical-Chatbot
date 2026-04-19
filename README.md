# Medical Chatbot

Medical Chatbot is an intelligent AI-powered assistant designed to help answer medical questions and provide health-related information. It uses a combination of:

- **PDF Documents**: Medical knowledge base stored as PDF files
- **Vector Database**: Pinecone stores and retrieves relevant medical documents instantly
- **Google Gemini AI**: Advanced language model that understands questions and provides accurate answers
- **Web Interface**: User-friendly chat interface to ask questions anytime

The chatbot reads your medical question, searches through the medical document database to find relevant information, and uses AI to generate a clear, concise answer in Vietnamese. This makes it easy for users to get quick medical information without having to search through multiple documents.

**Use Cases:**
- Get quick answers to common medical questions
- Learn about symptoms and treatments
- Access medical information in Vietnamese
- Understand health-related topics easily

## Features

- Chat interface for medical questions
- Retrieves answers from PDF documents
- Uses Google Gemini AI for responses
- Responds in Vietnamese
- Web-based interface with Flask

## Requirements

- Python 3.8+
- Google API Key (https://ai.google.dev)
- Pinecone API Key (https://www.pinecone.io)

## Installation

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd Medical-Chatbot
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file with your API keys
   ```
   PINECONE_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   ```

## How to Use

1. Place your medical PDF files in the `data/` folder

2. Build the index
   ```bash
   python store_index.py
   ```

3. Run the app
   ```bash
   python app.py
   ```

4. Open http://localhost:8080 in your browser

5. Ask medical questions in Vietnamese

## Project Structure

```
Medical-Chatbot/
├── app.py              # Main Flask app
├── store_index.py      # Build Pinecone index
├── requirements.txt    # Dependencies
├── data/               # Put PDFs here
├── src/
│   ├── helper.py       # PDF processing
│   └── prompt.py       # AI prompt
├── templates/
│   └── chat.html       # Chat interface
└── static/
    └── style.css       # Styling
```

## Technologies Used

- Flask - Web framework
- LangChain - AI framework
- Pinecone - Vector database
- Google Gemini - Language model
- HuggingFace - Embeddings
