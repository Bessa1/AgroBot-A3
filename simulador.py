import requests
import time
import random

# Endereço da sua API (Localhost)
URL_API = "http://127.0.0.1:5000/monitorar_safra"

culturas = ["Soja", "Milho", "Café Especial", "Algodão"]
setores = ["Estufa A", "Setor Norte", "Setor Sul"]

print("--- INICIANDO SIMULAÇÃO DE SENSORES IOT ---")
print("Pressione CTRL+C para parar.")

while True:
    # 1. Gera dados aleatórios (Simula a leitura do sensor)
    cultura = random.choice(culturas)
    setor = random.choice(setores)
    
    # Gera temperatura entre 15 e 40 graus
    temp = random.randint(15, 40) 
    # Gera umidade entre 20% e 90%
    umidade = random.randint(20, 90)

    payload = {
        "setor": setor,
        "cultura": cultura,
        "temp": temp,
        "umidade": umidade
    }

    # 2. Mostra no terminal o que está enviando
    print(f"\n📡 Sensor enviando: {cultura} ({temp}°C / {umidade}%) ...")

    # 3. Envia para a API e mostra a resposta
    try:
        response = requests.post(URL_API, json=payload)
        if response.status_code == 200:
            dados_resp = response.json()
            print(f" Resposta da API: {dados_resp['status']}")
        else:
            print(f" Erro na API: {response.status_code}")
    except:
        print(" Erro: Não foi possível conectar na API. Ela está rodando?")

    # Espera 5 segundos para o próximo envio
    time.sleep(5)