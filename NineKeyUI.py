import sys
from PySide6 import QtCore, QtWidgets, QtGui

import NineKey

class MainWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('9 Key Decoder')
		self.inputBox = QtWidgets.QLineEdit('Input Here.')
		self.resultBox = QtWidgets.QTextEdit('Result.')
		self.resultBox.setReadOnly(True)
		self.button = QtWidgets.QPushButton('Decode')

		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.inputBox)
		self.layout.addWidget(self.button)
		self.layout.addWidget(self.resultBox)

		self.button.clicked.connect(self.decode)

	@QtCore.Slot()
	def decode(self):
		result, err = NineKey.main(self.inputBox.text())
		if err != None:
			self.resultBox.setText(err)
		else:
			self.resultBox.setText(result)


if __name__ == '__main__':
	print('Initializing...')

	app = QtWidgets.QApplication([])

	widget = MainWidget()
	widget.resize(800, 600)
	widget.show()

	print('Running...')
	sys.exit(app.exec())