from flask import Flask, jsonify, request

app = Flask(__name__)
peers = []

@app.route('/register', methods=['POST'])
def register_peer():
    data = request.json
    ip = data.get('ip')
    if ip and ip not in peers:
        peers.append(ip)
        return jsonify({"status": "registered"}), 200
    return jsonify({"status": "already registered"}), 400

@app.route('/peers', methods=['GET'])
def list_peers():
    return jsonify({"peers": peers})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
