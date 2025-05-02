from flask import Flask, request
import requests

app = Flask(__name__)

# Ganti dengan URL Web App Apps Script-mu
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwbHdQjS5kl7F8RGdHJw9J2vLfiH8i1Ic9fGcARikBBIlbmXd6wzU3agArqEJgKpRej/exec"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.form.to_dict()
    # kirim ke Apps Script
    requests.post(GOOGLE_SCRIPT_URL, json=data)
    return "OK", 200

if __name__ == "__main__":
    app.run()
