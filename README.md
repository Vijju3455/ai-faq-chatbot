# AI FAQ Chatbot

A simple AI-powered FAQ chatbot built with Flask backend and vanilla JavaScript frontend.

## Features

- Simple keyword-based matching for FAQ responses
- RESTful API for chat functionality
- Clean, responsive chat interface
- CORS enabled for frontend-backend communication

## Project Structure

```
ai-faq-chatbot/
├── backend/
│   ├── app.py          # Flask API server
│   ├── faq_data.json   # FAQ data storage
│   └── chatbot.py      # Chatbot logic
├── frontend/
│   ├── index.html      # Chat interface HTML
│   ├── style.css       # Chat interface styling
│   └── script.js       # Frontend JavaScript
├── README.md           # Project documentation
└── TODO.md             # Development tasks
```

## Setup and Installation

1. Make sure you have Python 3.x installed.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the backend server:
   ```
   python backend/app.py
   ```

4. Open the frontend in your browser:
   - Open `frontend/index.html` in your web browser, or
   - Serve the frontend files using a local server (e.g., using Python's `http.server`):
     ```
     cd frontend
     python -m http.server 8000
     ```
     Then open `http://localhost:8000` in your browser.

## Usage

1. Start the backend server as described above.
2. Open the frontend in your browser.
3. Type your questions in the chat input and press Enter or click Send.
4. The chatbot will respond based on the FAQ data.

## API Endpoints

- `GET /faqs`: Returns all FAQ data
- `POST /chat`: Accepts a JSON payload with a "message" field and returns a chatbot response

## Customization

- Edit `backend/faq_data.json` to add or modify FAQ entries.
- Modify `backend/chatbot.py` to improve the matching algorithm.
- Update `frontend/style.css` to change the appearance of the chat interface.

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

This project is open source and available under the [MIT License](LICENSE).

