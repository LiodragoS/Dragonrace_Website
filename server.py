from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/<path:path>', methods=['GET'])
def serve_file(path):
    return send_from_directory('.', path)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    waiting_for_input = data.get('waiting_for_input')

    # Schreiben in die status.txt Datei
    with open('status.txt', 'w') as f:
        f.write(str(waiting_for_input))

    return jsonify({'status': 'success'}), 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)