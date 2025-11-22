from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from qfluentwidgets import FluentWindow, VBoxLayout, DisplayLabel
from subInterface.home_interface import HomeInterface

class MyWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        # 创建子界面
        self.homeInterface = HomeInterface(self)

        # 初始化窗口
        self.initWindow()
        # 初始化导航接口
        self.initNavigation()

        
    def initNavigation(self):
        self.addSubInterface(self.homeInterface, 'Home', 'Home')

    def initWindow(self):
        self.resize(960, 780)
        self.setMinimumSize(QSize(760, 300))
        self.setWindowTitle("Simple Markdown Editor")




if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()