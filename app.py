from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/json')
def get_json():
    data = {
        'message': 'Hello, this is a JSON response!',
        'status': 'success'
    }
    return jsonify(data)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
