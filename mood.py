from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import datetime
import time

app = Flask(__name__)

def get_bot_response(text):
    time.sleep(1.5)
    
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.txt", "a") as file:
        file.write(f"[{date}] Score: {score:.2f} | Text: {text}\n")

    if score > 0.5:
        return "That's awesome! Glad to hear it."
    elif score < -0.5:
        return "I'm sorry things are tough. I'm listening."
    else:
        return "I see. Tell me more."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_text = request.form["msg"]
    bot_reply = get_bot_response(user_text)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)