from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import AI_Agent
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize the AI Agent
agent = AI_Agent()

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        query = data.get('query')
        
        if not query:
            logging.error('Empty query received')
            return jsonify({'error': 'Query is required'}), 400
            
        logging.info(f'Received query: {query}')
        
        # Process the query using the AI Agent
        result = agent.solve(query)
        
        logging.info(f'Query result: {result}')
        return jsonify({'result': result})
        
    except Exception as e:
        error_message = str(e)
        logging.error(f'Error processing query: {error_message}')
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(port=5000)