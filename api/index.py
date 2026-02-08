from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def api():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    
    return jsonify({
    "ip": ip,
    "user-agent": user_agent
    })
    
if __name__ == "__main__":
    app.run(debug=True)
