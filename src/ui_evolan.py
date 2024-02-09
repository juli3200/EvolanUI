# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_evolan.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QFrame,
    QHBoxLayout, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQSlider import QCustomQSlider
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.Theme import (QLabelThemed, QPushButtonThemed)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 590)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo_label = QLabelThemed(self.header)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMaximumSize(QSize(50, 50))
        self.logo_label.setPixmap(QPixmap(u":/images/logo.png"))
        self.logo_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label)

        self.menuBtn = QPushButtonThemed(self.header)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/feather/Icons/feather/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.minimizeBtn = QPushButtonThemed(self.frame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/feather/Icons/feather/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButtonThemed(self.frame)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_regular/Icons/font_awesome/regular/window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButtonThemed(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/feather/Icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.horizontalLayout = QHBoxLayout(self.mainBody)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenu = QCustomSlideMenu(self.mainBody)
        self.sideMenu.setObjectName(u"sideMenu")
        self.sideMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.frame_2 = QFrame(self.sideMenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(195, 108))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.simulateBtn = QPushButtonThemed(self.frame_2)
        self.simulateBtn.setObjectName(u"simulateBtn")
        self.simulateBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome_regular/Icons/font_awesome/regular/circle-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.simulateBtn.setIcon(icon4)
        self.simulateBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.simulateBtn)

        self.renderBtn = QPushButtonThemed(self.frame_2)
        self.renderBtn.setObjectName(u"renderBtn")
        self.renderBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/font_awesome_solid/Icons/font_awesome/solid/gears.png", QSize(), QIcon.Normal, QIcon.Off)
        self.renderBtn.setIcon(icon5)
        self.renderBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.renderBtn)

        self.showBtn = QPushButtonThemed(self.frame_2)
        self.showBtn.setObjectName(u"showBtn")
        self.showBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/font_awesome_regular/Icons/font_awesome/regular/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showBtn.setIcon(icon6)
        self.showBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.showBtn)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sideMenu)

        self.stackedWidget = QCustomQStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.simulatePage = QWidget()
        self.simulatePage.setObjectName(u"simulatePage")
        self.simulatePage.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.simulatePage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.frame_3 = QFrame(self.simulatePage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_page1_simulate = QLabelThemed(self.frame_3)
        self.label_page1_simulate.setObjectName(u"label_page1_simulate")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_page1_simulate.setFont(font1)
        self.label_page1_simulate.setStyleSheet(u"")
        self.label_page1_simulate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_page1_simulate)

        self.openBtn = QPushButtonThemed(self.frame_3)
        self.openBtn.setObjectName(u"openBtn")
        self.openBtn.setMaximumSize(QSize(16777215, 16777215))
        self.openBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_regular/Icons/font_awesome/regular/folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBtn.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.openBtn, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frame_4 = QFrame(self.simulatePage)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_simulate_new = QLabelThemed(self.frame_4)
        self.label_simulate_new.setObjectName(u"label_simulate_new")
        self.label_simulate_new.setFont(font1)
        self.label_simulate_new.setStyleSheet(u"")
        self.label_simulate_new.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_simulate_new)

        self.formFrame = QFrame(self.frame_4)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setMinimumSize(QSize(350, 0))
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabelThemed(self.formFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.dimensionLabel = QLabelThemed(self.formFrame)
        self.dimensionLabel.setObjectName(u"dimensionLabel")
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(12)
        self.dimensionLabel.setFont(font2)
        self.dimensionLabel.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.dimensionLabel)

        self.dimensionLineEdit = QLineEdit(self.formFrame)
        self.dimensionLineEdit.setObjectName(u"dimensionLineEdit")
        self.dimensionLineEdit.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dimensionLineEdit)

        self.numberOfBotsLabel = QLabelThemed(self.formFrame)
        self.numberOfBotsLabel.setObjectName(u"numberOfBotsLabel")
        self.numberOfBotsLabel.setFont(font2)
        self.numberOfBotsLabel.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.numberOfBotsLabel)

        self.numberOfBotsLineEdit = QLineEdit(self.formFrame)
        self.numberOfBotsLineEdit.setObjectName(u"numberOfBotsLineEdit")
        self.numberOfBotsLineEdit.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.numberOfBotsLineEdit)

        self.generationLifetimeLabel = QLabelThemed(self.formFrame)
        self.generationLifetimeLabel.setObjectName(u"generationLifetimeLabel")
        self.generationLifetimeLabel.setFont(font2)
        self.generationLifetimeLabel.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.generationLifetimeLabel)

        self.generationLifetimeLineEdit = QLineEdit(self.formFrame)
        self.generationLifetimeLineEdit.setObjectName(u"generationLifetimeLineEdit")
        self.generationLifetimeLineEdit.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.generationLifetimeLineEdit)

        self.button_simulate_code = QPushButtonThemed(self.formFrame)
        self.button_simulate_code.setObjectName(u"button_simulate_code")
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(10)
        self.button_simulate_code.setFont(font3)
        self.button_simulate_code.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_simulate_code.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/feather/Icons/feather/code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_simulate_code.setIcon(icon8)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.button_simulate_code)

        self.button_simulate_advanced = QPushButtonThemed(self.formFrame)
        self.button_simulate_advanced.setObjectName(u"button_simulate_advanced")
        self.button_simulate_advanced.setFont(font3)
        self.button_simulate_advanced.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_simulate_advanced.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/font_awesome_solid/Icons/font_awesome/solid/sliders.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_simulate_advanced.setIcon(icon9)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.button_simulate_advanced)


        self.verticalLayout_4.addWidget(self.formFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.button_simulate_simulate = QPushButtonThemed(self.frame_4)
        self.button_simulate_simulate.setObjectName(u"button_simulate_simulate")
        self.button_simulate_simulate.setFont(font3)
        self.button_simulate_simulate.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_simulate_simulate.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/feather/Icons/feather/play-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_simulate_simulate.setIcon(icon10)

        self.verticalLayout_4.addWidget(self.button_simulate_simulate)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.simulatePage)
        self.renderPage = QWidget()
        self.renderPage.setObjectName(u"renderPage")
        self.renderPage.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.renderPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.renderPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_page1_simulate_2 = QLabelThemed(self.frame_5)
        self.label_page1_simulate_2.setObjectName(u"label_page1_simulate_2")
        self.label_page1_simulate_2.setFont(font1)
        self.label_page1_simulate_2.setStyleSheet(u"")
        self.label_page1_simulate_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_page1_simulate_2)


        self.verticalLayout_7.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.renderPage)
        self.showPage = QWidget()
        self.showPage.setObjectName(u"showPage")
        self.showPage.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.showPage)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.showPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_page1_simulate_3 = QLabelThemed(self.frame_6)
        self.label_page1_simulate_3.setObjectName(u"label_page1_simulate_3")
        self.label_page1_simulate_3.setFont(font1)
        self.label_page1_simulate_3.setStyleSheet(u"")
        self.label_page1_simulate_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_page1_simulate_3)

        self.openMediaBtn = QPushButtonThemed(self.frame_6)
        self.openMediaBtn.setObjectName(u"openMediaBtn")
        self.openMediaBtn.setMaximumSize(QSize(16777215, 16777215))
        self.openMediaBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/font_awesome_regular/Icons/font_awesome/regular/file-video.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openMediaBtn.setIcon(icon11)

        self.horizontalLayout_7.addWidget(self.openMediaBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.videoPlayerWidget = QWidget(self.showPage)
        self.videoPlayerWidget.setObjectName(u"videoPlayerWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.videoPlayerWidget.sizePolicy().hasHeightForWidth())
        self.videoPlayerWidget.setSizePolicy(sizePolicy1)
        self.videoLayout = QHBoxLayout(self.videoPlayerWidget)
        self.videoLayout.setObjectName(u"videoLayout")

        self.verticalLayout_6.addWidget(self.videoPlayerWidget)

        self.frame_15 = QFrame(self.showPage)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 5, 0)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(194, 42))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.playBtn = QPushButtonThemed(self.frame_17)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.playBtn.setIcon(icon10)
        self.playBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.playBtn, 0, Qt.AlignLeft)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(122, 40))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.prevMediaBtn = QPushButtonThemed(self.frame_18)
        self.prevMediaBtn.setObjectName(u"prevMediaBtn")
        self.prevMediaBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/feather/Icons/feather/skip-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prevMediaBtn.setIcon(icon12)
        self.prevMediaBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.prevMediaBtn)

        self.stopMediaBtn = QPushButtonThemed(self.frame_18)
        self.stopMediaBtn.setObjectName(u"stopMediaBtn")
        self.stopMediaBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/feather/Icons/feather/stop-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopMediaBtn.setIcon(icon13)
        self.stopMediaBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.stopMediaBtn)

        self.nextMediaBtn = QPushButtonThemed(self.frame_18)
        self.nextMediaBtn.setObjectName(u"nextMediaBtn")
        self.nextMediaBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/feather/Icons/feather/skip-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextMediaBtn.setIcon(icon14)
        self.nextMediaBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.nextMediaBtn)


        self.horizontalLayout_10.addWidget(self.frame_18, 0, Qt.AlignRight)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.frame_19, 0, Qt.AlignHCenter)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.frame_20, 0, Qt.AlignRight)


        self.horizontalLayout_8.addWidget(self.frame_17, 0, Qt.AlignLeft)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.playedMediaDuration = QLabelThemed(self.frame_21)
        self.playedMediaDuration.setObjectName(u"playedMediaDuration")

        self.horizontalLayout_15.addWidget(self.playedMediaDuration)

        self.mediaProgress = QCustomQSlider(self.frame_21)
        self.mediaProgress.setObjectName(u"mediaProgress")
        self.mediaProgress.setCursor(QCursor(Qt.PointingHandCursor))
        self.mediaProgress.setPageStep(1)
        self.mediaProgress.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.mediaProgress)

        self.totalMediaDuration = QLabelThemed(self.frame_21)
        self.totalMediaDuration.setObjectName(u"totalMediaDuration")

        self.horizontalLayout_15.addWidget(self.totalMediaDuration)


        self.horizontalLayout_8.addWidget(self.frame_21)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(122, 42))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.volumeBtn = QPushButtonThemed(self.frame_16)
        self.volumeBtn.setObjectName(u"volumeBtn")
        self.volumeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/feather/Icons/feather/volume-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.volumeBtn.setIcon(icon15)
        self.volumeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.volumeBtn)

        self.volumeSlider = QCustomQSlider(self.frame_16)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setPageStep(1)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.volumeSlider)


        self.horizontalLayout_8.addWidget(self.frame_16, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.videoFilesWidget = QListWidget(self.showPage)
        self.videoFilesWidget.setObjectName(u"videoFilesWidget")
        self.videoFilesWidget.setMaximumSize(QSize(16777215, 70))
        self.videoFilesWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.videoFilesWidget.setFlow(QListView.LeftToRight)
        self.videoFilesWidget.setProperty("isWrapping", True)
        self.videoFilesWidget.setSpacing(5)
        self.videoFilesWidget.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.videoFilesWidget)

        self.stackedWidget.addWidget(self.showPage)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.mainBody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label.setText("")
        self.menuBtn.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.simulateBtn.setText(QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.renderBtn.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        self.showBtn.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_page1_simulate.setText(QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"Open existing", None))
        self.label_simulate_new.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>New</p></body></html>", None))
        self.label_3.setText("")
        self.dimensionLabel.setText(QCoreApplication.translate("MainWindow", u"Dimension", None))
        self.numberOfBotsLabel.setText(QCoreApplication.translate("MainWindow", u"Number of bots", None))
        self.generationLifetimeLabel.setText(QCoreApplication.translate("MainWindow", u"Generation lifetime", None))
        self.button_simulate_code.setText(QCoreApplication.translate("MainWindow", u"Code...", None))
        self.button_simulate_advanced.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.button_simulate_simulate.setText(QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.label_page1_simulate_2.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        self.label_page1_simulate_3.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.openMediaBtn.setText(QCoreApplication.translate("MainWindow", u"Open videos", None))
        self.playBtn.setText("")
#if QT_CONFIG(shortcut)
        self.playBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.prevMediaBtn.setText("")
#if QT_CONFIG(shortcut)
        self.prevMediaBtn.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.stopMediaBtn.setText("")
#if QT_CONFIG(shortcut)
        self.stopMediaBtn.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.nextMediaBtn.setText("")
#if QT_CONFIG(shortcut)
        self.nextMediaBtn.setShortcut(QCoreApplication.translate("MainWindow", u"N", None))
#endif // QT_CONFIG(shortcut)
        self.playedMediaDuration.setText(QCoreApplication.translate("MainWindow", u"--:--", None))
        self.totalMediaDuration.setText(QCoreApplication.translate("MainWindow", u"--:--", None))
        self.volumeBtn.setText("")
    # retranslateUi

