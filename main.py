from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Serverless! Working\n", 200, {'Content-Type': 'text/plain'}

@app.route('/echo', methods=['POST'])
def echo():
    return jsonify({"status": "echo endpoint works"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)