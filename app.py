import os
from flask import Flask, request
from model import predict_lung
from werkzeug.exceptions import BadRequest, InternalServerError

app = Flask(__name__)

@app.errorhandler(BadRequest)
def bad_request_handler(error):
    return {
        "error": error.description
    }, 400


@app.errorhandler(InternalServerError)
def internal_server_error_handler(error):
    return {
        "error": error.description
    }, 500


@app.route("/predict", methods=['POST'])
def predict():
    file = request.files.get('image')
    if not file:
        return {
            "error": "Image is required"
        }, 400
    
    supported_mimetypes = ["image/jpeg", "image/png"]
    mimetype = file.content_type
    if mimetype not in supported_mimetypes:
        return {
            "error": "Unsupported image type"
        }, 415

    prediction = predict_lung(file)
    return {
        "result": prediction
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")