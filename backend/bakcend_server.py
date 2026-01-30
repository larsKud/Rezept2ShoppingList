from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

frontend_origin = "http://localhost:4200"
api_log_prefix = "API - "
app = Flask(__name__)
CORS(app, origins=[frontend_origin])


@app.route('/getData', methods=["GET"])
def get_data():
    data = [{'key': 'Banane', 'value': '15'},{'key': 'Balong', 'value': '0'}]
    response = make_response(data, 200)
    return response

if __name__ == "__main__":
    app.run(host="localhost", port="4000", debug=True)