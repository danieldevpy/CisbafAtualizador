import threading
import dados
from PyQt5 import uic, QtWidgets
import win32com.client as client
import files_rc
_ = files_rc

app = QtWidgets.QApplication([])
screen = uic.loadUi("grafic.ui")


def main():
    screen.listWidget.setStyleSheet("QListView::item:selected{""}")


def select_box():
    folder = screen.comboBox.currentText()
    screen.listWidget.clear()
    if folder != "SELECIONE":
        values = dados.list_folder(folder)
        for value in values:
            screen.listWidget.addItem(value)


def to_move():
    folder = screen.comboBox.currentText()
    if folder != "SELECIONE":
        values = dados.list_folder(folder)
        value_index = screen.listWidget.currentRow()
        if value_index != -1:
            screen.label_2.setText('A instalação logo começará! AGUARDE')
            screen.label_2.setStyleSheet('color: rgb(0, 115, 19);')
            item = values[value_index].split()
            new_file = item[0]
            shell = client.Dispatch("WScript.shell")
            t1 = threading.Thread(target=dados.to_move, args=(shell, screen, folder, new_file))
            t1.start()
        else:
            screen.label_2.setText('ERROR: Selecione um arquivo!')
            screen.label_2.setStyleSheet('color: red;')
    else:
        screen.label_2.setText('ERROR: Você não selecionou nada!')
        screen.label_2.setStyleSheet('color: red;')


screen.comboBox.activated.connect(select_box)
screen.pushButton.clicked.connect(to_move)
screen.listWidget.clicked.connect(main)
screen.show()
app.exec()
