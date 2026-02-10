import requests
import time
import os
from flask import Flask
from threading import Thread

# Token que você confirmou
TOKEN = "8330303692:AAFZj_VxjY0YGip1tTenySayLMVda-lu27k"

app = Flask('')
@app.route('/')
def home(): return "ROBO RICK AGUARDANDO ID"

def run_web():
    app.run(host='0.0.0.0', port=10000)

def buscar_id_e_enviar():
    print("🤖 Robô Rick - Modo busca de ID iniciado...")
    while True:
        try:
            # Verifica se alguém falou com o bot ou se ele foi adicionado a um grupo
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
            res = requests.get(url).json()
            if res["result"]:
                # Pega o ID da última conversa que o bot teve
                ultimo_chat_id = res["result"][-1]["message"]["chat"]["id"]
                print(f"✅ ID ENCONTRADO: {ultimo_chat_id}")
                
                # Tenta enviar a mensagem para esse ID encontrado
                msg_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                requests.post(msg_url, json={"chat_id": ultimo_chat_id, "text": f"🚀 RICK! O ID REAL É: {ultimo_chat_id}"})
                break
        except: pass
        time.sleep(5)

if __name__ == "__main__":
    Thread(target=run_web).start()
    buscar_id_e_enviar()
