from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from qfluentwidgets import FluentWindow, VBoxLayout, DisplayLabel
from subInterface.edit_area_interface import EditAreaInterface
from subInterface.document_interface import DocumentInterface
from subInterface.edit_interface import EditInterface
from subInterface.viewer_interface import ViewerInterface
from subInterface.help_interface import HelpInterface
from subInterface.setting_interface import SettingInterface
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import NavigationItemPosition

class MyWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        # 创建子界面
        self.editAreaInterface = EditAreaInterface(self)
        self.documentInterface = DocumentInterface(self)
        self.editInterface = EditInterface(self)
        self.viewerInterface = ViewerInterface(self)
        self.helpInterface = HelpInterface(self)
        self.settingInterface = SettingInterface(self)

        # 初始化窗口
        self.initWindow()
        # 初始化导航接口
        self.initNavigation()

        
    def initNavigation(self):
        pos = NavigationItemPosition.SCROLL
        self.addSubInterface(self.editAreaInterface, FIF.CODE, 'Write')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.documentInterface, FIF.DOCUMENT, "文件", pos)
        self.addSubInterface(self.editInterface, FIF.EDIT, "编辑", pos)
        self.addSubInterface(self.viewerInterface, FIF.VIEW, "视图", pos)
        self.addSubInterface(self.helpInterface, FIF.HELP, "帮助", NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settingInterface, FIF.SETTING, "设置", NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(960, 780)
        self.setMinimumSize(QSize(760, 300))
        self.setWindowTitle("Simple Markdown Editor")




if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()