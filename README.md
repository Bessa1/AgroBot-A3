# 🌱 AgroBot - Monitoramento Inteligente de Safras (IoT)

> **Status:** ✅ Concluído | **Versão:** 1.0

## 📖 Sobre o Projeto
O **AgroBot** é um sistema de monitoramento agrícola baseado em IoT (Internet das Coisas). O objetivo é simular sensores de campo que coletam dados de temperatura e umidade em tempo real e, através de uma API Gateway desenvolvida em Python, analisar riscos para culturas sensíveis (como Soja e Café).

Caso condições críticas sejam detectadas (Geada ou Estresse Térmico), o sistema aciona alertas instantâneos via **Telegram** para o agrônomo responsável, permitindo uma tomada de decisão rápida (Data-Driven Decision).

---

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando práticas modernas de Engenharia de Software e Cloud:

* ![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python) **Core:** Linguagem principal do backend.
* ![Flask](https://img.shields.io/badge/Flask-Microframework-lightgrey?style=flat&logo=flask) **API:** Responsável por receber e processar os dados dos sensores.
* ![Requests](https://img.shields.io/badge/Requests-Lib-orange) **Simulação:** Script para gerar dados sintéticos de sensores IoT.
* ![Telegram](https://img.shields.io/badge/Telegram-API-blue?style=flat&logo=telegram) **Notificações:** Integração para alertas em tempo real.
* ![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-black?style=flat&logo=github) **Ambiente:** Desenvolvimento e execução 100% na nuvem.

---

## ⚙️ Arquitetura da Solução

O fluxo de dados segue o padrão de **API Gateway**:

1.  **Sensores (Simulador):** Geram dados aleatórios de temperatura/umidade e enviam via POST.
2.  **API (Servidor):** Recebe o JSON, aplica as Regras de Negócio (ex: Café não suporta > 32°C).
3.  **Bot (Telegram):** Se a regra for violada, o bot notifica o usuário final.

---

## 🛠️ Como Executar (Passo a Passo)

Para o sistema funcionar, precisamos rodar dois processos simultâneos: o **Servidor (API)** e o **Simulador (Sensores)**. Siga a ordem abaixo:

### 1️⃣ Preparação do Ambiente
Ao abrir o terminal (no VS Code ou GitHub Codespaces), instale as dependências necessárias:
```bash
pip install -r requirements.txt


