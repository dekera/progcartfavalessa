from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import sys

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Minha aplicacao")

botao = QPushButton("Clique aqui")

def ao_clicar():
    QMessageBox.information(janela, "Aviso", "Botão clicado!")

botao.clicked.connect(ao_clicar)

layout = QVBoxLayout()
layout.addWidget(botao)
janela.setLayout(layout)

janela.show()

sys.exit(app.exec())