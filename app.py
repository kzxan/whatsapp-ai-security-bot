from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip().lower()

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "salem":
        msg.body("Сәлем! Мен AI қауіпсіздік жүйесінің WhatsApp ботымын.")
    elif incoming_msg == "menu":
        msg.body("Командалар:\n1) salem\n2) menu\n3) komek")
    elif incoming_msg == "komek":
        msg.body("Бұл бот қауіпсіздік жүйесі туралы хабарламалар жібереді.")
    else:
        msg.body(f"Сіз жаздыңыз: {incoming_msg}")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)