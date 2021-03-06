# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm:\Programs\Python\Konverter\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMaximumSize(QtCore.QSize(700, 600))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(60, 20, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setUnderline(False)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.browse_sel_file_btn = QtWidgets.QToolButton(self.centralwidget)
        self.browse_sel_file_btn.setGeometry(QtCore.QRect(290, 90, 41, 31))
        self.browse_sel_file_btn.setObjectName("browse_sel_file_btn")
        self.browse_sel_file_lbl = QtWidgets.QLabel(self.centralwidget)
        self.browse_sel_file_lbl.setGeometry(QtCore.QRect(30, 80, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.browse_sel_file_lbl.setFont(font)
        self.browse_sel_file_lbl.setObjectName("browse_sel_file_lbl")
        self.sel_file_path_disp = QtWidgets.QLabel(self.centralwidget)
        self.sel_file_path_disp.setGeometry(QtCore.QRect(260, 150, 421, 31))
        self.sel_file_path_disp.setText("")
        self.sel_file_path_disp.setObjectName("sel_file_path_disp")
        self.sel_file_path_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sel_file_path_lbl.setGeometry(QtCore.QRect(30, 140, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.sel_file_path_lbl.setFont(font)
        self.sel_file_path_lbl.setObjectName("sel_file_path_lbl")
        self.conv_frm_lbl = QtWidgets.QLabel(self.centralwidget)
        self.conv_frm_lbl.setGeometry(QtCore.QRect(30, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.conv_frm_lbl.setFont(font)
        self.conv_frm_lbl.setObjectName("conv_frm_lbl")
        self.conv_to_lbl = QtWidgets.QLabel(self.centralwidget)
        self.conv_to_lbl.setGeometry(QtCore.QRect(350, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.conv_to_lbl.setFont(font)
        self.conv_to_lbl.setObjectName("conv_to_lbl")
        self.browse_conv_file_lbl = QtWidgets.QLabel(self.centralwidget)
        self.browse_conv_file_lbl.setGeometry(QtCore.QRect(30, 260, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.browse_conv_file_lbl.setFont(font)
        self.browse_conv_file_lbl.setObjectName("browse_conv_file_lbl")
        self.browse_conv_file_btn = QtWidgets.QToolButton(self.centralwidget)
        self.browse_conv_file_btn.setGeometry(QtCore.QRect(420, 270, 41, 31))
        self.browse_conv_file_btn.setObjectName("browse_conv_file_btn")
        self.suffix_lbl = QtWidgets.QLabel(self.centralwidget)
        self.suffix_lbl.setGeometry(QtCore.QRect(30, 320, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.suffix_lbl.setFont(font)
        self.suffix_lbl.setObjectName("suffix_lbl")
        self.suffix_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.suffix_line_edit.setGeometry(QtCore.QRect(240, 330, 131, 31))
        self.suffix_line_edit.setObjectName("suffix_line_edit")
        self.conv_frm_box = QtWidgets.QComboBox(self.centralwidget)
        self.conv_frm_box.setGeometry(QtCore.QRect(210, 210, 69, 31))
        self.conv_frm_box.setObjectName("conv_frm_box")
        self.conv_frm_box.addItem("")
        self.conv_frm_box.addItem("")
        self.conv_frm_box.addItem("")
        self.conv_frm_box.addItem("")
        self.conv_frm_box.addItem("")
        self.conv_to_box = QtWidgets.QComboBox(self.centralwidget)
        self.conv_to_box.setGeometry(QtCore.QRect(500, 210, 69, 31))
        self.conv_to_box.setObjectName("conv_to_box")
        self.conv_to_box.addItem("")
        self.conv_to_box.addItem("")
        self.conv_to_box.addItem("")
        self.conv_to_box.addItem("")
        self.progress_lbl = QtWidgets.QLabel(self.centralwidget)
        self.progress_lbl.setGeometry(QtCore.QRect(30, 380, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.progress_lbl.setFont(font)
        self.progress_lbl.setObjectName("progress_lbl")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(170, 390, 501, 31))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.conv_new_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.conv_new_file_btn.setGeometry(QtCore.QRect(480, 500, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.conv_new_file_btn.setFont(font)
        self.conv_new_file_btn.setObjectName("conv_new_file_btn")
        self.estimated_time_disp = QtWidgets.QLabel(self.centralwidget)
        self.estimated_time_disp.setGeometry(QtCore.QRect(30, 450, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.estimated_time_disp.setFont(font)
        self.estimated_time_disp.setObjectName("estimated_time_disp")
        self.estimated_time_lbl = QtWidgets.QLabel(self.centralwidget)
        self.estimated_time_lbl.setGeometry(QtCore.QRect(220, 450, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.estimated_time_lbl.setFont(font)
        self.estimated_time_lbl.setObjectName("estimated_time_lbl")
        self.file_name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.file_name_lbl.setGeometry(QtCore.QRect(380, 80, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setItalic(True)
        self.file_name_lbl.setFont(font)
        self.file_name_lbl.setObjectName("file_name_lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView_Supported_Formats = QtWidgets.QMenu(self.menuHelp)
        self.menuView_Supported_Formats.setObjectName("menuView_Supported_Formats")
        self.menuContact_Developer = QtWidgets.QMenu(self.menuHelp)
        self.menuContact_Developer.setObjectName("menuContact_Developer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionStyle_Configurator = QtWidgets.QAction(MainWindow)
        self.actionStyle_Configurator.setObjectName("actionStyle_Configurator")
        self.actionRead_Manual = QtWidgets.QAction(MainWindow)
        self.actionRead_Manual.setObjectName("actionRead_Manual")
        self.actionCheck_out_Github = QtWidgets.QAction(MainWindow)
        self.actionCheck_out_Github.setObjectName("actionCheck_out_Github")
        self.actionVisit_Website = QtWidgets.QAction(MainWindow)
        self.actionVisit_Website.setObjectName("actionVisit_Website")
        self.actionVideo = QtWidgets.QAction(MainWindow)
        self.actionVideo.setObjectName("actionVideo")
        self.actionAudio = QtWidgets.QAction(MainWindow)
        self.actionAudio.setObjectName("actionAudio")
        self.actionDocuments = QtWidgets.QAction(MainWindow)
        self.actionDocuments.setObjectName("actionDocuments")
        self.actionSuggest_Improvements = QtWidgets.QAction(MainWindow)
        self.actionSuggest_Improvements.setObjectName("actionSuggest_Improvements")
        self.actionContribute_on_Github = QtWidgets.QAction(MainWindow)
        self.actionContribute_on_Github.setObjectName("actionContribute_on_Github")
        self.actionBuy_Dev_a_Coffee = QtWidgets.QAction(MainWindow)
        self.actionBuy_Dev_a_Coffee.setObjectName("actionBuy_Dev_a_Coffee")
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuEdit.addAction(self.actionStyle_Configurator)
        self.menuView_Supported_Formats.addAction(self.actionVideo)
        self.menuView_Supported_Formats.addAction(self.actionAudio)
        self.menuView_Supported_Formats.addAction(self.actionDocuments)
        self.menuContact_Developer.addAction(self.actionSuggest_Improvements)
        self.menuContact_Developer.addAction(self.actionContribute_on_Github)
        self.menuContact_Developer.addAction(self.actionBuy_Dev_a_Coffee)
        self.menuHelp.addAction(self.actionRead_Manual)
        self.menuHelp.addAction(self.actionCheck_out_Github)
        self.menuHelp.addAction(self.actionVisit_Website)
        self.menuHelp.addAction(self.menuContact_Developer.menuAction())
        self.menuHelp.addAction(self.menuView_Supported_Formats.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Select File to convert or Drag and Drop Anywhere!"))
        self.browse_sel_file_btn.setText(_translate("MainWindow", "..."))
        self.browse_sel_file_lbl.setText(_translate("MainWindow", "Browse File to Convert : "))
        self.sel_file_path_lbl.setText(_translate("MainWindow", "Selected File Path : "))
        self.conv_frm_lbl.setText(_translate("MainWindow", "Convert From : "))
        self.conv_to_lbl.setText(_translate("MainWindow", "Convert To : "))
        self.browse_conv_file_lbl.setText(_translate("MainWindow", "Browse Converted File Destination :"))
        self.browse_conv_file_btn.setText(_translate("MainWindow", "..."))
        self.suffix_lbl.setText(_translate("MainWindow", "Suffix to New File : "))
        self.suffix_line_edit.setText(_translate("MainWindow", "_konverted"))
        self.conv_frm_box.setItemText(0, _translate("MainWindow", "MP4"))
        self.conv_frm_box.setItemText(1, _translate("MainWindow", "MOV"))
        self.conv_frm_box.setItemText(2, _translate("MainWindow", "MKV"))
        self.conv_frm_box.setItemText(3, _translate("MainWindow", "AVI"))
        self.conv_frm_box.setItemText(4, _translate("MainWindow", "M4A"))
        self.conv_to_box.setItemText(0, _translate("MainWindow", "MP3"))
        self.conv_to_box.setItemText(1, _translate("MainWindow", "WAV"))
        self.conv_to_box.setItemText(2, _translate("MainWindow", "FLV"))
        self.conv_to_box.setItemText(3, _translate("MainWindow", "OGG"))
        self.progress_lbl.setText(_translate("MainWindow", "Progress : "))
        self.conv_new_file_btn.setText(_translate("MainWindow", "Convert Another File"))
        self.estimated_time_disp.setText(_translate("MainWindow", "Estimated Time  : "))
        self.estimated_time_lbl.setText(_translate("MainWindow", "00:00:59"))
        self.file_name_lbl.setText(_translate("MainWindow", "filename.sth"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView_Supported_Formats.setTitle(_translate("MainWindow", "View Supported Formats"))
        self.menuContact_Developer.setTitle(_translate("MainWindow", "Contact Developer"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionOpen.setText(_translate("MainWindow", "Open New File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionStyle_Configurator.setText(_translate("MainWindow", "Style Configurator"))
        self.actionRead_Manual.setText(_translate("MainWindow", "Read Manual"))
        self.actionCheck_out_Github.setText(_translate("MainWindow", "Read Code on Github"))
        self.actionVisit_Website.setText(_translate("MainWindow", "Visit Website"))
        self.actionVideo.setText(_translate("MainWindow", "Video"))
        self.actionAudio.setText(_translate("MainWindow", "Audio"))
        self.actionDocuments.setText(_translate("MainWindow", "Documents"))
        self.actionSuggest_Improvements.setText(_translate("MainWindow", "Suggest Improvements"))
        self.actionContribute_on_Github.setText(_translate("MainWindow", "Contribute on Github"))
        self.actionBuy_Dev_a_Coffee.setText(_translate("MainWindow", "Buy him a Mentos!"))
