from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    return jsonify({"result": data['a'] + data['b']})

if __name__ == '__main__':
    app.run(debug=True)