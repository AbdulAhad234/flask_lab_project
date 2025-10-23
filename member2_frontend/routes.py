"""
Frontend routes and API endpoints
This file contains route suggestions for the backend developer to integrate
"""

from flask import render_template, request, jsonify

def register_frontend_routes(app):
    """
    Function to register all frontend-related routes
    Backend developer should integrate this into main/app.py
    """
    
    @app.route('/')
    def home():
        """Homepage route that renders the main template"""
        return render_template('index.html')
    
    @app.route('/health')
    def health():
        """Health check endpoint"""
        return "OK", 200
    
    @app.route('/data', methods=['POST'])
    def receive_data():
        """Endpoint to receive and process data"""
        data = request.get_json()
        
        if not data or 'data' not in data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Process the data (backend developer can add more logic)
        received_data = data['data']
        
        return jsonify({
            'message': 'Data received successfully',
            'received': received_data
        }), 200