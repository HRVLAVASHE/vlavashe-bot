import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Замените на ваш токен от BotFather
TOKEN = "7766534579:AAGz6aNo8l81LVw8n2Ml9L5kpBt11WEYBfQ"
URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route(f"/{TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    chat_id = data["message"]["chat"]["id"]
    message_text = data["message"].get("text", "")

    # Ответ на команды или сообщения
    if message_text == "/start":
        reply = "Привет! Я помогу ответить на ваши вопросы."
    else:
        reply = f"Вы написали: {message_text}"

    # Отправляем ответ
    send_message(chat_id, reply)
    return "OK"

def send_message(chat_id, text):
    url = f"{URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))
