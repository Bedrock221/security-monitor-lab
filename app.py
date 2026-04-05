from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Security Lab is Active. Monitoring..."

# This is the "Trap" endpoint that captures data
@app.route('/capture', methods=['POST'])
def capture():
    # Capture the JSON data sent by a link or script
    data = request.get_json()
    
    # In a real attack, they log this to a file or database
    print(f"--- DATA CAPTURED ---")
    print(f"User/Token: {data}")
    
    return jsonify({"status": "success", "info": "Data logged safely"}), 200

if __name__ == "__main__":
    # Render uses the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
