# Rastreador de Veículos (Desktop - Python + OpenStreetMap)

Este é um aplicativo desktop feito em Python para rastrear veículos em tempo real, usando **links de localização enviados pelo WhatsApp** e exibindo tudo em um **mapa interativo gratuito (OpenStreetMap via Folium)**.

## ✅ Recursos

- Interface gráfica com PyQt5
- Exibe localização de vários veículos simultaneamente
- Não precisa de chave API nem cartão
- Funciona com links do Google Maps (`https://www.google.com/maps?q=-15.6,-47.7`)

## 🚀 Como usar

1. Instale as dependências:

```bash
pip install folium PyQt5 PyQtWebEngine
```

2. Execute o app:

```bash
python rastreador.py
```

3. Cole o link do WhatsApp e o nome/ID do veículo.
4. Clique em "Adicionar Veículo" e veja no mapa.

## 📌 Exemplo de link válido

```
https://www.google.com/maps?q=-15.7797,-47.9297
```

## 🗺️ Tecnologia usada

- Python 3.x
- PyQt5 + QtWebEngine
- Folium (OpenStreetMap)

---

Criado com ❤️ por Master e sua assistente.
