import requests
import time
import os
from flask import Flask
from threading import Thread

# Dados do Rick
TOKEN = "8330303692:AAFZj_VxjY0YGip1tTenySayLMVda-lu27k"
CHAT_ID = "-1003824589908"
API_URL = "https://blaze.com/api/singleplayer-originals/originals/slide/recent"

app = Flask('')
@app.route('/')
def home():
    return "Robô Rick Mentoria 2.0 Online"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

def enviar_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except: pass

def robo_principal():
    enviar_telegram("✅ CONEXÃO ESTABELECIDA!\nO robô da Mentoria 2.0 está no ar.")
    ultima_rodada_id = ""
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(API_URL, headers=headers, timeout=15).json()
            id_atual = response[0]['id']
            if id_atual != ultima_rodada_id:
                ultima_rodada_id = id_atual
                v1, v2, v3 = float(response[1]['slide_point']), float(response[2]['slide_point']), float(response[3]['slide_point'])
                if v1 < 1.50 and v2 < 1.50 and v3 < 1.50:
                    enviar_telegram("🚨 **SINAL CONFIRMADO** 🚨\n\n🎯 Alvo: 2.00x\n🛡️ Gale: 1")
        except: pass
        time.sleep(15)

if __name__ == "__main__":
    Thread(target=run_web).start()
    robo_principal()
