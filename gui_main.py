# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QPushButton, QMainWindow, QWidget, QLabel, QVBoxLayout, QCheckBox, QAction, QMenuBar, QMenu, QHBoxLayout, QProgressBar
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QIcon


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(481, 447)

    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet(open('style.css').read())
        self.progressbar = QProgressBar(self.centralwidget)
        self.progressbar.setGeometry(QRect(20, 10, 441, 20))
        self.progressbar.setStyleSheet(open('style.css').read())

        self.label_info = QLabel(self.centralwidget)
        self.label_info.setGeometry(QRect(20, 35, 441, 15))

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(20, 55, 121, 271))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_9 = QCheckBox(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.checkBox_9)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QRect(170, 55, 131, 271))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_10 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_10)
        self.checkBox_11 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_11)
        self.checkBox_12 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_12)
        self.checkBox_13 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_13)
        self.checkBox_14 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_14)
        self.checkBox_15 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_15)
        self.checkBox_16 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_16)
        self.checkBox_17 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_17)
        self.checkBox_18 = QCheckBox(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.checkBox_18)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QRect(330, 55, 131, 271))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_19 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_19)
        self.checkBox_20 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_20)
        self.checkBox_21 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_21)
        self.checkBox_22 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_22)
        self.checkBox_23 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_23)
        self.checkBox_24 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_24)
        self.checkBox_25 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_25)
        self.checkBox_26 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_26)
        self.checkBox_27 = QCheckBox(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.checkBox_27)

        self.label_note = QLabel(self.centralwidget)
        self.label_note.setGeometry(QRect(20, 330, 350, 16))
        self.label_space = QLabel(self.centralwidget)
        self.label_space.setGeometry(QRect(20, 350, 350, 16))
        self.label_size = QLabel(self.centralwidget)
        self.label_size.setGeometry(QRect(155, 350, 350, 16))

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 380, 220, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_select_all = QPushButton(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.button_select_all)
        self.button_select_all.setStyleSheet(open('style.css').read())
        self.button_select_all.setMinimumSize(100, 30)
        self.button_select_all.setProperty('class', 'Aqua')
        self.button_deselect_all = QPushButton(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.button_deselect_all)
        self.button_deselect_all.setStyleSheet(open('style.css').read())
        self.button_deselect_all.setMinimumSize(100, 30)
        self.button_deselect_all.setProperty('class', 'Aqua')

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QRect(354, 380, 107, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_uninstall = QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.button_uninstall)
        self.button_uninstall.setStyleSheet(open('style.css').read())
        self.button_uninstall.setMinimumSize(100, 30)
        self.button_uninstall.setProperty('class', 'Grapefruit')

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 481, 21))
        self.menuHelp = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.actionRefresh = QAction(self)
        self.actionHomepage = QAction(self)
        self.actionAbout = QAction(self)
        self.actionQuit = QAction(self)
        self.menuHelp.addAction(self.actionRefresh)
        self.menuHelp.addAction(self.actionHomepage)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionQuit)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.setStyleSheet(open('style.css').read())

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "PyDebloatX"))

        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionRefresh.setText(_translate("MainWindow", "&Refresh"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionHomepage.setText(_translate("MainWindow", "&Github"))
        self.actionHomepage.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

        self.label_info.setText(_translate("MainWindow", "Refreshing list of installed apps..."))

        self.checkBox.setText(_translate("MainWindow", "3D Builder"))
        self.checkBox_2.setText(_translate("MainWindow", "3D Viewer"))
        self.checkBox_3.setText(_translate("MainWindow", "Alarms and Clock"))
        self.checkBox_4.setText(_translate("MainWindow", "Calculator"))
        self.checkBox_5.setText(_translate("MainWindow", "Calendar and Mail"))
        self.checkBox_6.setText(_translate("MainWindow", "Camera"))
        self.checkBox_7.setText(_translate("MainWindow", "Get Help"))
        self.checkBox_8.setText(_translate("MainWindow", "Groove Music"))
        self.checkBox_9.setText(_translate("MainWindow", "Maps"))

        self.checkBox_10.setText(_translate("MainWindow", "Messaging"))
        self.checkBox_11.setText(_translate("MainWindow", "Money"))
        self.checkBox_12.setText(_translate("MainWindow", "Movies && TV"))
        self.checkBox_13.setText(_translate("MainWindow", "News"))
        self.checkBox_14.setText(_translate("MainWindow", "Office"))
        self.checkBox_15.setText(_translate("MainWindow", "OneNote"))
        self.checkBox_16.setText(_translate("MainWindow", "Paint 3D"))
        self.checkBox_17.setText(_translate("MainWindow", "People"))
        self.checkBox_18.setText(_translate("MainWindow", "Photos"))

        self.checkBox_19.setText(_translate("MainWindow", "Skype"))
        self.checkBox_20.setText(_translate("MainWindow", "Solitaire"))
        self.checkBox_21.setText(_translate("MainWindow", "Sports"))
        self.checkBox_22.setText(_translate("MainWindow", "Tips"))
        self.checkBox_23.setText(_translate("MainWindow", "Voice Recorder"))
        self.checkBox_24.setText(_translate("MainWindow", "Weather"))
        self.checkBox_25.setText(_translate("MainWindow", "Windows Feedback"))
        self.checkBox_26.setText(_translate("MainWindow", "Xbox"))
        self.checkBox_27.setText(_translate("MainWindow", "Your Phone"))

        self.label_note.setText(_translate("MainWindow", "NOTE: Microsoft Edge and Cortana cannot be uninstalled using this GUI."))
        self.label_space.setText(_translate("MainWindow", "Total amount of disk space:"))
        self.label_size.setText(_translate("MainWindow", "0 MB"))

        self.button_select_all.setText(_translate("MainWindow", "Select All"))
        self.button_deselect_all.setText(_translate("MainWindow", "Deselect All"))

        self.button_uninstall.setText(_translate("MainWindow", "Uninstall"))

        self.checkBox.setToolTip('View, create, and personalize 3D objects.')
        self.checkBox_2.setToolTip('View 3D models and animations in real-time.')
        self.checkBox_3.setToolTip('A combination of alarm clock, world clock, timer, and stopwatch.')
        self.checkBox_4.setToolTip('A calculator that includes standard, scientific, and programmer modes, as well as a unit converter.')
        self.checkBox_5.setToolTip('Stay up to date with email and schedule managing.')
        self.checkBox_6.setToolTip('Point and shoot to take pictures on Windows 10.')
        self.checkBox_7.setToolTip('Provide a way to ask a question and get recommended solutions or contact assisted support.')
        self.checkBox_8.setToolTip('Listen to music on Windows, iOS, and Android devices.')
        self.checkBox_9.setToolTip('Search for places to get directions, business info, and reviews.')

        self.checkBox_10.setToolTip('Quick, reliable SMS, MMS and RCS messaging from your phone.')
        self.checkBox_11.setToolTip('Finance calculators, currency exchange rates and commodity prices from around the world.')
        self.checkBox_12.setToolTip('All your movies and TV shows, all in one place, on all your devices.')
        self.checkBox_13.setToolTip('Deliver breaking news and trusted, in-depth reporting from the world\'s best journalists.')
        self.checkBox_14.setToolTip('Find all your Office apps and files in one place.')
        self.checkBox_15.setToolTip('Digital notebook for capturing and organizing everything across your devices.')
        self.checkBox_16.setToolTip('Make 2D masterpieces or 3D models that you can play with from all angles.')
        self.checkBox_17.setToolTip('Connect with all your friends, family, colleagues, and acquaintances in one place.')
        self.checkBox_18.setToolTip('View and edit your photos and videos, make movies, and create albums.')

        self.checkBox_19.setToolTip('Instant message, voice or video call application.')
        self.checkBox_20.setToolTip('Solitaire is one of the most played computer card games of all time.')
        self.checkBox_21.setToolTip('Live scores and in-depth game experiences for more than 150 leagues.')
        self.checkBox_22.setToolTip('Provide users with information and tips about operating system features.')
        self.checkBox_23.setToolTip('Record sounds, lectures, interviews, and other events.')
        self.checkBox_24.setToolTip('Latest weather conditions, accurate 10-day and hourly forecasts.')
        self.checkBox_25.setToolTip('Provide feedback about Windows and apps by sharing suggestions or problems.')
        self.checkBox_26.setToolTip('Browse the catalogue, view recommendations, and discover PC games with Xbox Game Pass.')
        self.checkBox_27.setToolTip('Link your Android phone and PC to view and reply to text messages, access mobile apps, and receive notifications.')
