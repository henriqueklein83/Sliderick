import requests
import time
import os
from flask import Flask
from threading import Thread

# CONFIGURAÇÕES DO RICK
TOKEN = "8330303692:AAFZj_VxjY0YGip1tTenySayLMVda-lu27k"
CHAT_ID = -1003824589908 # SE NÃO FUNCIONAR, TESTE COM: -4660784
API_URL = "https://blaze.com/api/singleplayer-originals/originals/slide/recent"

app = Flask('')
@app.route('/')
def home(): return "ROBO RICK ONLINE"

def enviar_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except: pass

def loop_principal():
    # TESTE IMEDIATO
    enviar_telegram("🚀 **SISTEMA INICIALIZADO!**\nO Robô da Mentoria 2.0 já está monitorando o Slide.")
    
    ultima_rodada_id = ""
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(API_URL, headers=headers, timeout=15).json()
            id_atual = response[0]['id']
            
            if id_atual != ultima_rodada_id:
                ultima_rodada_id = id_atual
                v1 = float(response[1]['slide_point'])
                v2 = float(response[2]['slide_point'])
                v3 = float(response[3]['slide_point'])
                
                # ESTRATÉGIA: 3 velas abaixo de 1.50
                if v1 < 1.50 and v2 < 1.50 and v3 < 1.50:
                    enviar_telegram("🚨 **SINAL CONFIRMADO** 🚨\n\n🎯 Alvo: 2.00x\n🛡️ Gale: 1")
        except: pass
        time.sleep(15)

if __name__ == "__main__":
    Thread(target=lambda: app.run(host='0.0.0.0', port=10000)).start()
    loop_principal()