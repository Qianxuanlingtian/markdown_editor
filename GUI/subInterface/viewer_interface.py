from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import VBoxLayout, DisplayLabel, ScrollArea, ComboBox, PushButton


class ViewerInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('viewerInterface')

        # self.scrollArea1 = ScrollArea(self)
        # self.scrollArea2 = ScrollArea(self)

        self.verticalLayout = VBoxLayout(self)

        self.widgetContents1 = QWidget(self)
        self.widgetContents1.setObjectName('widgetContents1')
        self.widgetContents1vBoxLayout = VBoxLayout(self.widgetContents1)
        self.widgetContents1vBoxLayout.setContentsMargins(0,0,0,36)
        self.widgetContents1vBoxLayout.setSpacing(40)

        self.widgetContents1vBoxLayout.addWidget(QLabel('测试使用'))
        self.widgetContents1vBoxLayout.addWidget(PushButton('测试使用'))
        self.testComboBox = ComboBox()
        self.testComboBox.addItems(['测试1', '测试2', '测试3', '测试4'])
        self.widgetContents1vBoxLayout.addWidget(self.testComboBox)
        
        self.setWidget(self.widgetContents1)
        self.setWidgetResizable(True)