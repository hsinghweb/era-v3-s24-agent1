# Math Agent Chrome Extension

A Chrome extension that performs mathematical calculations using a local Math Agent server powered by Google's Gemini AI model.

## Features

- Factorial calculations (0! to n!)
- Sum of number lists
- Fibonacci sequence generation
- ASCII code conversions
- Exponential calculations
- Real-time calculation results
- User-friendly interface

## Prerequisites

- Google Chrome browser
- Python 3.x
- Google Gemini API key

## Installation

### Backend Server Setup

1. Clone this repository
2. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
3. Install Python dependencies:
   ```bash
   pip install flask flask-cors python-dotenv google-generativeai
   ```
4. Start the server:
   ```bash
   python server.py
   ```
   The server will run on `http://localhost:5000`

### Chrome Extension Setup

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" in the top right
3. Click "Load unpacked" and select the extension directory
4. The Math Agent icon should appear in your Chrome toolbar

## Usage

1. Click the Math Agent icon in your Chrome toolbar
2. Enter your mathematical query in the input field
3. Click "Calculate" or press Enter
4. View the result in the popup window

## Architecture

- **Frontend**: Chrome extension with popup interface (HTML, CSS, JavaScript)
- **Backend**: Flask server with Google Gemini AI integration
- **API**: RESTful endpoint at `/calculate` for processing queries

## Error Handling

- The extension provides visual feedback for errors
- Server logs are maintained in `server.log`
- Math Agent logs are stored in `math_agent.log`

## Security

- CORS enabled for localhost connections only
- API key stored securely in `.env` file
- Input validation on both frontend and backend