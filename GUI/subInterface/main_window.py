from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication

from qfluentwidgets import FluentWindow, NavigationItemPosition, SplashScreen
from qfluentwidgets import FluentIcon as FIF

from common.translator import Translator
from .edit_area_interface import EditAreaInterface
from .document_interface import DocumentInterface
from .edit_interface import EditInterface
from .viewer_interface import ViewerInterface
from .help_interface import HelpInterface
from .setting_interface import SettingInterface

class MyWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        # 初始化窗口
        self.initWindow()

        # 创建子界面
        # self.editAreaInterface = EditAreaInterface(self)
        # self.documentInterface = DocumentInterface(self)
        # self.editInterface = EditInterface(self)
        self.viewerInterface = ViewerInterface(self)
        # self.helpInterface = HelpInterface(self)
        # self.settingInterface = SettingInterface(self)

        # 使亚克力效果生效
        self.navigationInterface.setAcrylicEnabled(True)

        # 初始化导航接口
        self.initNavigation()
        self.splashSreen.finish()

    def initNavigation(self):
        # 添加导航组件
        t = Translator()

        pos = NavigationItemPosition.SCROLL
        # self.addSubInterface(self.editAreaInterface, FIF.CODE, 'Write')
        self.navigationInterface.addSeparator()
        # self.addSubInterface(self.documentInterface, FIF.DOCUMENT, "文件", pos)
        # self.addSubInterface(self.editInterface, FIF.EDIT, "编辑", pos)
        self.addSubInterface(self.viewerInterface, FIF.VIEW, "视图", pos)
        # self.addSubInterface(self.helpInterface, FIF.HELP, "帮助", NavigationItemPosition.BOTTOM)
        # self.addSubInterface(self.settingInterface, FIF.SETTING, "设置", NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(960, 780)
        self.setMinimumSize(QSize(760, 300))
        self.setWindowTitle("Simple Markdown Editor")

        # 创建启动画面
        self.splashSreen = SplashScreen(self.windowIcon(), self)
        self.splashSreen.setIconSize(QSize(106, 106))
        self.splashSreen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.show()
        QApplication.processEvents()