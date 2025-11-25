from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import VBoxLayout, DisplayLabel

class EditInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.view = QWidget()
        self.vboxlayout = QVBoxLayout(self.view)

        self.initWidget()

    def initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('editInterface')
        
        self.setLayout(self.vboxlayout)
