from time import sleep
from flask import Flask
from email import message
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
from chat import get_response
from time import sleep

app = Flask(__name__)
CORS(app)

@app.route("/")
def index_get():
    return render_template("base.html")

@app.route("/predict",methods=["POST"])
def predict():

    text = request.get_json().get("message")
    response = get_response(text)
    sleep(1)
    message = {"answer":response}
    return jsonify(message)



if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="localhost", port=5000, debug=True)