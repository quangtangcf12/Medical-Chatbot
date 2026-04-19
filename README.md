# Medical Chatbot

An AI chatbot that answers medical questions using PDF documents stored in Pinecone vector database.

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

## Author

Tran Tri Duc - 22520276@gm.uit.edu.vn
