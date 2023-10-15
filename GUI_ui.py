# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1031, 703)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1031, 703))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.background = QFrame(Form)
        self.background.setObjectName(u"background")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy1)
        self.background.setMinimumSize(QSize(1020, 680))
        self.background.setStyleSheet(u"")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.prompt_line = QLabel(self.background)
        self.prompt_line.setObjectName(u"prompt_line")
        self.prompt_line.setGeometry(QRect(20, 0, 981, 31))
        self.layoutWidget = QWidget(self.background)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 1001, 641))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_block = QFrame(self.layoutWidget)
        self.left_block.setObjectName(u"left_block")
        self.left_block.setMaximumSize(QSize(300, 16777215))
        self.left_block.setFrameShape(QFrame.StyledPanel)
        self.left_block.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.left_block)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 300, 241, 271))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.girl_pic = QLabel(self.layoutWidget1)
        self.girl_pic.setObjectName(u"girl_pic")
        sizePolicy.setHeightForWidth(self.girl_pic.sizePolicy().hasHeightForWidth())
        self.girl_pic.setSizePolicy(sizePolicy)
        self.girl_pic.setMinimumSize(QSize(200, 200))
        self.girl_pic.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.girl_pic.setScaledContents(True)
        self.girl_pic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.girl_pic)

        self.upload_girl = QPushButton(self.layoutWidget1)
        self.upload_girl.setObjectName(u"upload_girl")

        self.verticalLayout_2.addWidget(self.upload_girl)

        self.layoutWidget2 = QWidget(self.left_block)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 0, 241, 271))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.human_pic = QLabel(self.layoutWidget2)
        self.human_pic.setObjectName(u"human_pic")
        self.human_pic.setEnabled(True)
        sizePolicy.setHeightForWidth(self.human_pic.sizePolicy().hasHeightForWidth())
        self.human_pic.setSizePolicy(sizePolicy)
        self.human_pic.setMinimumSize(QSize(200, 200))
        self.human_pic.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.human_pic.setScaledContents(True)
        self.human_pic.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.human_pic)

        self.upload_human = QPushButton(self.layoutWidget2)
        self.upload_human.setObjectName(u"upload_human")

        self.verticalLayout.addWidget(self.upload_human)


        self.horizontalLayout_2.addWidget(self.left_block)

        self.mid_block = QFrame(self.layoutWidget)
        self.mid_block.setObjectName(u"mid_block")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mid_block.sizePolicy().hasHeightForWidth())
        self.mid_block.setSizePolicy(sizePolicy2)
        self.mid_block.setMinimumSize(QSize(200, 200))
        self.mid_block.setFrameShape(QFrame.StyledPanel)
        self.mid_block.setFrameShadow(QFrame.Raised)
        self.random_gen = QPushButton(self.mid_block)
        self.random_gen.setObjectName(u"random_gen")
        self.random_gen.setGeometry(QRect(40, 220, 121, 31))
        self.random_gen.setStyleSheet(u"")
        self.start_blend = QPushButton(self.mid_block)
        self.start_blend.setObjectName(u"start_blend")
        self.start_blend.setGeometry(QRect(40, 270, 121, 31))

        self.horizontalLayout_2.addWidget(self.mid_block)

        self.right_block = QFrame(self.layoutWidget)
        self.right_block.setObjectName(u"right_block")
        self.right_block.setMaximumSize(QSize(300, 16777215))
        self.right_block.setFrameShape(QFrame.StyledPanel)
        self.right_block.setFrameShadow(QFrame.Raised)
        self.layoutWidget3 = QWidget(self.right_block)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 140, 258, 288))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.output_pic = QLabel(self.layoutWidget3)
        self.output_pic.setObjectName(u"output_pic")
        sizePolicy.setHeightForWidth(self.output_pic.sizePolicy().hasHeightForWidth())
        self.output_pic.setSizePolicy(sizePolicy)
        self.output_pic.setMinimumSize(QSize(256, 256))
        self.output_pic.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.output_pic.setScaledContents(True)
        self.output_pic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.output_pic)

        self.save_image = QPushButton(self.layoutWidget3)
        self.save_image.setObjectName(u"save_image")

        self.verticalLayout_7.addWidget(self.save_image)


        self.horizontalLayout_2.addWidget(self.right_block)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.prompt_line.setText(QCoreApplication.translate("Form", u"choose your photo and an anime girl photo", None))
        self.girl_pic.setText(QCoreApplication.translate("Form", u"input anime girl face", None))
        self.upload_girl.setText(QCoreApplication.translate("Form", u"import", None))
        self.human_pic.setText(QCoreApplication.translate("Form", u"input human face", None))
        self.upload_human.setText(QCoreApplication.translate("Form", u"import", None))
        self.random_gen.setText(QCoreApplication.translate("Form", u"random", None))
        self.start_blend.setText(QCoreApplication.translate("Form", u"Blend!", None))
        self.output_pic.setText(QCoreApplication.translate("Form", u"output", None))
        self.save_image.setText(QCoreApplication.translate("Form", u"save image", None))
    # retranslateUi

