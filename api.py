from flask import Flask,jsonify,request
from ModelController import get_prediction

app = Flask(__name__)

@app.route("/character-recog",methods=["POST"])

def predict_data():
    image = request.files.get("Characters")
    prediction = get_prediction(image)

    return jsonify({
        "prediction":prediction
    }),200

if __name__ == "main":
    app.run(debug=True)




