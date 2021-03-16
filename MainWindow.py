import os

import moviepy.editor as mp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, Qt, QThread, QUrl, pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QListWidget, QMainWindow

# class Worker(QObject):
#     '''
#     Worker thread

#     :param args: Arguments to make available to the run code
#     :param kwargs: Keywords arguments to make available to the run code

#     '''

#     def __init__(self, audio_format, src_file_path, suffix, dest_file_path):
#         super(Worker, self).__init__()
#         self.audio_format = audio_format
#         self.src_file_path = src_file_path
#         self.dest_file_path = dest_file_path
#         self.suffix = suffix
#         self.run()

#     @pyqtSlot()
#     def run(self):
#         '''
#         Initialise the runner function with passed self.args, self.kwargs.
#         '''
#         print('he he he i am converting it like anything!')
#         print('the selected audio format is {}'.format(self.audio_format))
#         my_clip = mp.VideoFileClip(self.src_file_path)
#         my_clip.audio.write_audiofile(self.dest_file_path + '\\' + self.src_file_path.split('/')[-1] +
#         self.suffix + '.' + self.audio_format.lower())


class cust_font(QtGui.QFont):
    def __init__(self):
        super().__init__()
        self.setFamily('Times New Roman')
        self.setPointSize(16)

    @classmethod  # say you get the pay as string values intead of integers
    def from_string(cls, num):
        list1 = []
        for i in range(num):
            list1.append(cls())
        return list1


class MainUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(700, 600)
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setupUi()
        self.dest_file_path = os.getcwd()
        self.def_conv_format = '.mp3'
        self.suffix = '_konverted'

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))

            self.src_file_path = links[0]
            self.file_name_lbl.setText(self.src_file_path.split('/')[-1][-30:])
            self.sel_file_path_disp.setText(self.src_file_path[-50:])
            print(self.src_file_path)
        else:
            event.ignore()

    def convert(self, audio_format):
        """Converts the Video file into `audio_format` using Moviepy

        Args:
            audio_format (string): Any audio format, without '.'
        """
        my_clip = mp.VideoFileClip(self.src_file_path)
        my_clip.audio.write_audiofile(self.dest_file_path + '\\' + self.src_file_path.split('/')[-1] +
                                      self.suffix + '.' + audio_format.lower())

    def show_src_dialog(self):
        fname, _ = QFileDialog.getOpenFileUrl(
            self, filter='Video (*.mp4 *.mkv *.avi *.m4a *.mov)')
        self.src_file_path = fname.toLocalFile()
        self.file_name_lbl.setText(self.src_file_path.split('/')[-1][-30:])
        self.sel_file_path_disp.setText(self.src_file_path[-50:])
        print(self.src_file_path)

    def show_dest_dialog(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.dest_file_path = fname
        print(self.dest_file_path)

    def start(self):
        audio_format = self.conv_to_box.currentText()
        self.suffix = self.suffix_line_edit.text()
        self.clicked('Initializing convertion now!')
        self.convert(audio_format)

    def setupUi(self):

        ## Fonts ##
        title_font, font_16, font_18 = cust_font.from_string(3)
        title_font.setFamily("Georgia")
        title_font.setBold(True)
        # font_16.setFamily("Calibre")
        font_16.setPointSize(16)
        # font_18.setFamily("Calibre")
        font_18.setPointSize(18)
        ## Labels ##

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(60, 20, 800, 41))

        self.title_label.setFont(title_font)
        self.title_label.setObjectName("title_label")
        self.browse_sel_file_btn = QtWidgets.QToolButton(self.centralwidget)
        self.browse_sel_file_btn.setGeometry(QtCore.QRect(290, 90, 41, 31))
        self.browse_sel_file_btn.setObjectName("browse_sel_file_btn")
        self.browse_sel_file_lbl = QtWidgets.QLabel(self.centralwidget)
        self.browse_sel_file_lbl.setGeometry(QtCore.QRect(30, 80, 271, 51))
        self.browse_sel_file_btn.clicked.connect(
            lambda: self.show_src_dialog())
        self.browse_sel_file_lbl.setFont(font_18)
        self.browse_sel_file_lbl.setObjectName("browse_sel_file_lbl")

        self.sel_file_path_disp = QtWidgets.QLabel(self.centralwidget)
        self.sel_file_path_disp.setGeometry(QtCore.QRect(240, 150, 500, 31))
        self.sel_file_path_disp.setText("No File Selected")
        self.sel_file_path_disp.setFont(font_16)
        self.sel_file_path_disp.setObjectName("sel_file_path_disp")

        self.sel_file_path_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sel_file_path_lbl.setGeometry(QtCore.QRect(30, 140, 211, 51))
        self.sel_file_path_lbl.setFont(font_18)
        self.sel_file_path_lbl.setObjectName("sel_file_path_lbl")
        self.conv_to_lbl = QtWidgets.QLabel(self.centralwidget)
        self.conv_to_lbl.setGeometry(QtCore.QRect(30, 200, 171, 51))

        self.conv_to_lbl.setFont(font_18)
        self.conv_to_lbl.setObjectName("conv_to_lbl")

        self.browse_conv_file_lbl = QtWidgets.QLabel(self.centralwidget)
        self.browse_conv_file_lbl.setGeometry(QtCore.QRect(30, 260, 421, 51))

        self.browse_conv_file_lbl.setFont(font_18)
        self.browse_conv_file_lbl.setObjectName("browse_conv_file_lbl")
        self.browse_conv_file_btn = QtWidgets.QToolButton(self.centralwidget)
        self.browse_conv_file_btn.setGeometry(QtCore.QRect(420, 270, 41, 31))
        self.browse_conv_file_btn.setObjectName("browse_conv_file_btn")
        self.browse_conv_file_btn.clicked.connect(
            lambda: self.show_dest_dialog())

        self.suffix_lbl = QtWidgets.QLabel(self.centralwidget)
        self.suffix_lbl.setGeometry(QtCore.QRect(30, 320, 221, 51))

        self.suffix_lbl.setFont(font_18)
        self.suffix_lbl.setObjectName("suffix_lbl")
        self.suffix_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.suffix_line_edit.setGeometry(QtCore.QRect(240, 330, 131, 31))
        self.suffix_line_edit.setObjectName("suffix_line_edit")

        print(self.suffix_line_edit.text())

        self.conv_to_box = QtWidgets.QComboBox(self.centralwidget)
        self.conv_to_box.setGeometry(QtCore.QRect(210, 210, 69, 31))
        self.conv_to_box.setObjectName("conv_to_box")

        self.conv_to_box.addItems(['MP3', 'WAV', 'OGG', 'AAC'])
        self.progress_lbl = QtWidgets.QLabel(self.centralwidget)
        self.progress_lbl.setGeometry(QtCore.QRect(30, 380, 171, 51))

        self.progress_lbl.setFont(font_18)
        self.progress_lbl.setObjectName("progress_lbl")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(170, 390, 600, 31))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(550, 500, 201, 41))
        self.start_btn.clicked.connect(lambda: self.start())

        self.start_btn.setFont(font_18)
        self.estimated_time_disp = QtWidgets.QLabel(self.centralwidget)
        self.estimated_time_disp.setGeometry(QtCore.QRect(30, 450, 181, 51))

        self.estimated_time_disp.setFont(font_18)
        self.estimated_time_disp.setObjectName("estimated_time_disp")
        self.estimated_time_lbl = QtWidgets.QLabel(self.centralwidget)
        self.estimated_time_lbl.setGeometry(QtCore.QRect(220, 450, 151, 51))

        self.estimated_time_lbl.setFont(font_18)
        self.estimated_time_lbl.setObjectName("estimated_time_lbl")
        self.file_name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.file_name_lbl.setGeometry(QtCore.QRect(380, 80, 281, 51))

        font_16.setItalic(True)

        self.file_name_lbl.setFont(font_16)
        self.file_name_lbl.setObjectName("file_name_lbl")

        font_16.setItalic(False)

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView_Supported_Formats = QtWidgets.QMenu(self.menuHelp)
        self.menuView_Supported_Formats.setObjectName(
            "menuView_Supported_Formats")
        self.menuContact_Developer = QtWidgets.QMenu(self.menuHelp)
        self.menuContact_Developer.setObjectName("menuContact_Developer")

        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.actionNew_Window = QtWidgets.QAction(self)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtWidgets.QAction(self)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionStyle_Configurator = QtWidgets.QAction(self)
        self.actionStyle_Configurator.setObjectName("actionStyle_Configurator")
        self.actionRead_Manual = QtWidgets.QAction(self)
        self.actionRead_Manual.setObjectName("actionRead_Manual")
        self.actionCheck_out_Github = QtWidgets.QAction(self)
        self.actionCheck_out_Github.setObjectName("actionCheck_out_Github")
        self.actionVisit_Website = QtWidgets.QAction(self)
        self.actionVisit_Website.setObjectName("actionVisit_Website")
        self.actionVideo = QtWidgets.QAction(self)
        self.actionVideo.setObjectName("actionVideo")
        self.actionAudio = QtWidgets.QAction(self)
        self.actionAudio.setObjectName("actionAudio")
        self.actionDocuments = QtWidgets.QAction(self)
        self.actionDocuments.setObjectName("actionDocuments")
        self.actionSuggest_Improvements = QtWidgets.QAction(self)
        self.actionSuggest_Improvements.setObjectName(
            "actionSuggest_Improvements")
        self.actionContribute_on_Github = QtWidgets.QAction(self)
        self.actionContribute_on_Github.setObjectName(
            "actionContribute_on_Github")
        self.actionBuy_Dev_a_Coffee = QtWidgets.QAction(self)
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

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Konvert", "Konvert"))
        self.title_label.setText(_translate(
            "Konvert", "Select File to convert or Drag and Drop Anywhere!"))
        self.browse_sel_file_btn.setText(_translate("Konvert", "..."))
        self.browse_sel_file_lbl.setText(_translate(
            "Konvert", "Browse File to Convert : "))
        self.sel_file_path_lbl.setText(
            _translate("Konvert", "Selected File Path : "))
        self.conv_to_lbl.setText(_translate("Konvert", "Convert To : "))
        self.browse_conv_file_lbl.setText(_translate(
            "Konvert", "Browse Converted File Destination :"))
        self.browse_conv_file_btn.setText(_translate("Konvert", "..."))
        self.suffix_lbl.setText(_translate("Konvert", "Suffix to New File : "))
        self.suffix_line_edit.setText(_translate("Konvert", "_konverted"))
        self.progress_lbl.setText(_translate("Konvert", "Progress : "))
        self.start_btn.setText(_translate("Konvert", "Start"))
        self.estimated_time_disp.setText(
            _translate("Konvert", "Estimated Time  : "))
        self.estimated_time_lbl.setText(_translate("Konvert", "00:00:59"))
        self.file_name_lbl.setText(_translate("Konvert", ""))
        self.menuFile.setTitle(_translate("Konvert", "File"))
        self.menuEdit.setTitle(_translate("Konvert", "Edit"))
        self.menuHelp.setTitle(_translate("Konvert", "Help"))
        self.menuView_Supported_Formats.setTitle(
            _translate("Konvert", "View Supported Formats"))
        self.menuContact_Developer.setTitle(
            _translate("Konvert", "Contact Developer"))
        self.actionNew_Window.setText(_translate("Konvert", "New Window"))
        self.actionOpen.setText(_translate("Konvert", "Open New File"))
        self.actionExit.setText(_translate("Konvert", "Exit"))
        self.actionPreferences.setText(_translate("Konvert", "Preferences"))
        self.actionStyle_Configurator.setText(
            _translate("Konvert", "Style Configurator"))
        self.actionRead_Manual.setText(_translate("Konvert", "Read Manual"))
        self.actionCheck_out_Github.setText(
            _translate("Konvert", "Read Code on Github"))
        self.actionVisit_Website.setText(
            _translate("Konvert", "Visit Website"))
        self.actionVideo.setText(_translate("Konvert", "Video"))
        self.actionAudio.setText(_translate("Konvert", "Audio"))
        self.actionDocuments.setText(_translate("Konvert", "Documents"))
        self.actionSuggest_Improvements.setText(
            _translate("Konvert", "Suggest Improvements"))
        self.actionContribute_on_Github.setText(
            _translate("Konvert", "Contribute on Github"))
        self.actionBuy_Dev_a_Coffee.setText(
            _translate("Konvert", "Buy him a Mentos!"))

    def clicked(self, text):
        print(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # self = QtWidgets.Qself()
    ui = MainUI()
    # ui.setupUi(self)
    ui.show()
    sys.exit(app.exec_())
