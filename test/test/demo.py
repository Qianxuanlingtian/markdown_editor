from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from qfluentwidgets import VBoxLayout, ComboBox, CheckBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建界面上的组件
        self.cbbox = ComboBox()
        self.cbbox.addItems(['a', 'b', 'c'])
        self.ckbox = CheckBox()
        self.ckbox.setText("CheckBox")

        # 创建布局
        self.mainlayout = VBoxLayout(self)
        self.setLayout(self.mainlayout)

        self.hboxlayout1 = QHBoxLayout()
        self.hboxlayout2 = QHBoxLayout()

        # 向指定的布局上放置组件
        self.hboxlayout1.addWidget(self.cbbox)
        self.hboxlayout1.addWidget(self.ckbox)
        self.mainlayout.addLayout(self.hboxlayout1)

        # 信号触发
        self.bind()

    # 各个组件的信号触发槽函数
    def bind(self):
        '''各个组件的信号触发槽函数'''
        self.cbbox.currentIndexChanged.connect(self.comboBoxCurrentTextPrint)
        self.ckbox.checkStateChanged.connect(self.checkBoxCurrentStatePrint)

    # 各个槽函数的实现
    def comboBoxCurrentTextPrint(self):
        print(self.cbbox.currentText())

    def checkBoxCurrentStatePrint(self, state):
        print(state)
        if self.ckbox.isChecked():
            print (self.ckbox.text())

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()