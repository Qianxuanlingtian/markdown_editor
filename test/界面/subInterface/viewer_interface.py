from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import VBoxLayout, DisplayLabel, ScrollArea


class ViewerInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.view = QWidget()
        self.vboxlayout = QVBoxLayout(self.view)

        self.initWidget()

    def initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('viewerInterface')
        
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vboxlayout.setContentsMargins(0,0,0,36)
        self.vboxlayout.setSpacing(40)
        self.vboxlayout.addWidget(QLabel('测试使用'))