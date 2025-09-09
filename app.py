from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/json')
def get_json():
    data = {
        'message': 'Hello, this is a JSON response!',
        'status': 'success'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
