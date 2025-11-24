from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# --- SUAS CONFIGURAÇÕES (PREENCHA AQUI) ---
TELEGRAM_TOKEN = "8108541302:AAGLfN26dC2i41ooAKLGtLOwbECg1Vv2OfI"
CHAT_ID = "1543925291"  

def enviar_telegram(mensagem):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": mensagem})
    except:
        print("Erro ao enviar Telegram (Verifique internet ou Token)")

@app.route('/monitorar_safra', methods=['POST'])
def monitorar_safra():
    # 1. Recebe os dados do "Sensor"
    dados = request.json
    setor = dados.get('setor')
    cultura = dados.get('cultura')
    temp = float(dados.get('temp'))
    umidade = float(dados.get('umidade'))

    print(f" Recebido: {cultura} | {temp}°C | {umidade}%")

    # 2. Lógica Agronômica (Regras de Negócio)
    alerta = False
    
    # Regra: Soja/Café não gosta de calor extremo (>32) e seco (<40)
    if temp > 32 and umidade < 40:
        alerta = True
        msg_telegram = (
            f" **ALERTA CRÍTICO: ESTRESSE TÉRMICO** \n"
            f"--------------------------------\n"
            f" **Setor:** {setor}\n"
            f" **Cultura:** {cultura}\n"
            f" **Temperatura:** {temp}°C (Muito Alta)\n"
            f" **Umidade:** {umidade}% (Muito Baixa)\n"
            f" **Ação Automática:** Irrigação ligada!"
        )
        status_resposta = "CRÍTICO - Irrigação Ativada"
    
    # Regra: Frio extremo (<10)
    elif temp < 10:
        alerta = True
        msg_telegram = (
            f" **ALERTA DE GEADA** \n"
            f"--------------------------------\n"
            f" **Setor:** {setor}\n"
            f" **Cultura:** {cultura}\n"
            f" **Temperatura:** {temp}°C\n"
            f" **Ação Automática:** Aquecedores ligados!"
        )
        status_resposta = "CRÍTICO - Aquecimento Ativado"
    
    else:
        status_resposta = "NORMAL - Condições Ideais"

    # 3. Envia o alerta se necessário
    if alerta:
        enviar_telegram(msg_telegram)

    return jsonify({"status": status_resposta, "temp_atual": temp})

if __name__ == '__main__':
    # Roda a API na porta 5000
    app.run(host='0.0.0.0', port=5000)