from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import VBoxLayout, DisplayLabel

class BannerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)

        self.vboxLayout = QVBoxLayout(self)
        self.headerlabel = DisplayLabel('Simple Markdown Editor')
        self.headerlabel.setObjectName('headerlabel')

        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setContentsMargins(0, 20, 0, 0)
        self.vboxLayout.addWidget(self.headerlabel)
        self.vboxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)


class EditAreaInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = BannerWidget()
        self.view = QWidget()
        self.vboxlayout = QVBoxLayout(self.view)

        self.initWidget()

    def initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('homeInterface')
        
        self.setLayout(self.vboxlayout)
        self.vboxlayout.addWidget(self.banner)