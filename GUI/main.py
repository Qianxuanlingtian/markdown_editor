from PySide6.QtWidgets import QApplication

from qfluentwidgets import setTheme, Theme

from subInterface.main_window import MyWindow

if __name__ == "__main__":
    app = QApplication()
    setTheme(Theme.LIGHT)
    window = MyWindow()
    window.show()
    app.exec()