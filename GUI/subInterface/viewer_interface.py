from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import (QPixmap, QPainter, QPainterPath, QLinearGradient, QColor,
                            QBrush)
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from qfluentwidgets import  FluentIcon, ScrollArea

from common.link_card import LinkCardView
from common.config import HELP_URL, REPO_URL, EXAMPLE_URL, FEEDBACK_URL
from common.style_sheet import StyleSheet

class BannerWidget(QWidget):
    """ Banner Widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)

        self.vboxLayout = QVBoxLayout(self)
        self.viewLabel = QLabel('Viewer Interface', self)
        self.banner = QPixmap('GUI/resource/images/header1.png')
        self.linkCardView = LinkCardView(self)

        self.viewLabel.setObjectName('viewLabel')

        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setContentsMargins(0, 20, 0, 0)
        self.vboxLayout.addWidget(self.viewLabel)
        self.vboxLayout.addWidget(self.linkCardView, 1, Qt.AlignmentFlag.AlignBottom)
        self.vboxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.linkCardView.addCard(
            'GUI/resource/images/logo.png',
            self.tr('Getting Started'),
            self.tr('An overview of app development options and samples.'),
            HELP_URL
        )

        self.linkCardView.addCard(
            FluentIcon.GITHUB,
            self.tr('Github repo'),
            self.tr(
                'The latest fluent design controls and styles for your applications.'
            ),
            REPO_URL
        )

        self.linkCardView.addCard(
            FluentIcon.CODE,
            self.tr('Code samples'),
            self.tr(
                'Find samples that demonstrate specific tasks, features and APIs.'
            ),
            EXAMPLE_URL
        )

        self.linkCardView.addCard(
            FluentIcon.FEEDBACK,
            self.tr('Send feedback'),
            self.tr('Help us improve PyQt-Fluent-Widgets by providing feedback.'),
            FEEDBACK_URL
        )
    
    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.RenderHint.SmoothPixmapTransform | QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.FillRule.WindingFill)
        w, h = self.width(), self.height()
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
        path = path.simplified()

        # init linear gradient effect
        gradient = QLinearGradient(0, 0, 0, h)

        gradient.setColorAt(0, QColor(0, 0, 0, 255))
        gradient.setColorAt(1, QColor(0, 0, 0, 0))

        painter.fillPath(path, QBrush(gradient))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        painter.fillPath(path, QBrush(pixmap))


class ViewerInterface(ScrollArea):
    """View Interface"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = BannerWidget(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.view.setObjectName('view')
        self.setObjectName('viewerInterface')
        StyleSheet.VIEW_INTERFACE.apply(self)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)