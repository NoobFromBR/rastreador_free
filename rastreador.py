
import folium
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import re
import os

MAP_FILE = "map.html"

class MapaRastreamento(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rastreamento de Veículos (OpenStreetMap)")
        self.setGeometry(100, 100, 800, 600)
        self.veiculos = {}

        layout = QVBoxLayout()

        self.input_link = QLineEdit(self)
        self.input_link.setPlaceholderText("Cole o link de localização (Google Maps)")
        self.input_nome = QLineEdit(self)
        self.input_nome.setPlaceholderText("Nome/ID do veículo")
        self.botao_adicionar = QPushButton("Adicionar Veículo", self)
        self.botao_adicionar.clicked.connect(self.adicionar_veiculo)
        self.lista_veiculos = QListWidget(self)
        self.view = QWebEngineView(self)

        self.map = folium.Map(location=[-15.7797, -47.9297], zoom_start=4)
        self.salvar_mapa()
        # QWebEngineView.load espera um QUrl. Usar uma string causa erro em tempo de execução
        # em alguns ambientes. Por isso carregamos o arquivo através de QUrl.fromLocalFile
        self.view.load(QUrl.fromLocalFile(os.path.abspath(MAP_FILE)))

        layout.addWidget(self.input_link)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.botao_adicionar)
        layout.addWidget(self.lista_veiculos)
        layout.addWidget(self.view)
        self.setLayout(layout)

    def salvar_mapa(self):
        self.map.save(MAP_FILE)

    def adicionar_veiculo(self):
        link = self.input_link.text().strip()
        nome = self.input_nome.text().strip()
        match = re.search(r"q=(-?\d+\.\d+),(-?\d+\.\d+)", link)
        if not match or not nome:
            return
        lat, lng = float(match.group(1)), float(match.group(2))
        self.veiculos[nome] = (lat, lng)
        self.map = folium.Map(location=[lat, lng], zoom_start=6)
        for nome, (lat, lng) in self.veiculos.items():
            folium.Marker([lat, lng], popup=nome).add_to(self.map)
        self.salvar_mapa()
        self.view.load(QUrl.fromLocalFile(os.path.abspath(MAP_FILE)))
        self.lista_veiculos.clear()
        self.lista_veiculos.addItems(self.veiculos.keys())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MapaRastreamento()
    janela.show()
    sys.exit(app.exec_())
