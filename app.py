import sys
from PyQt5.QtWidgets import QApplication,  QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from pytube import Playlist, YouTube, exceptions
from main_window import Ui_MainWindow
from smart_mode_dialog import Ui_Dialog
from format_dialog import Dialog
from hurry.filesize import size, alternative

class FormatDialog(Dialog):
    def __init__(self):
        super().__init__()
        Dialog.__init__(self)
        
        self.setupUi(self)
        self.format_combox_2.addItems(['Download Video', 'Extract Audio'])
        self.format_combox_2.currentTextChanged.connect(self.current_text)
        self.current_text()
    
    def current_text(self):
        self.choosed_format = self.format_combox_2.currentText()

class SmartDialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        Ui_Dialog.__init__(self)
    
        self.setupUi(self)
         

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.__init__(self)
    
        self.setupUi(self)
        self.smart_mode_dialog = None

        self.tableWidget.setColumnWidth(0, 250)

        
        self.links = list()
        self.smart_mode.clicked.connect(self.smart_mode_slot)
        self.paste_link.clicked.connect(self.get_format)

        #self.action_series.triggered.connect(self.on_action_series)

    def smart_mode_slot(self):
        if self.smart_mode_dialog == None:
            self.smart_mode_dialog = Smart_Dialog()
            self.smart_mode_dialog.show()

        else:
            self.smart_mode_dialog.close()
            self.smart_mode_dialog = None

    def paste(self):
        QApplication.clipboard().dataChanged.connect(QApplication.clipboard().text)
        text = QApplication.clipboard().text()
        return text
        

    def get_yt_video(self):
        url = self.paste()
        try:
            yt = YouTube(url)
        except exceptions.VideoUnavailable:
            print(f'Video {url} is unavaialable, skipping.')
            self.show_info_box(f'Video {url} is unavaialable', 'Unavaialable Video')
        except exceptions.RegexMatchError:
            print(f'Video {url} is unavaialable, skipping.')
            # msgBox.buttonClicked.connect(msgButtonClick)
            self.show_info_box("No valid link was found in the clipboard.\n\nCopy the video link from the browser address bar and then click 'Paste Link' again.", 'Video Not Found')
        else:
            print(f'Video link is: {url}')
            return yt
    
    def show_info_box(self, infos:str, title:str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(infos)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
    
    def show_detail_dialog(self):
        pass



    def get_format(self):
        yt = self.get_yt_video()
        if yt :
            self.format = FormatDialog()
            choosed_format = self.format.choosed_format
            if choosed_format == 'Extract Audio':
                self.extract_audio(yt, self.format)
            else:
                self.dowload_video(yt, self.format)

    def extract_audio(self, yt, format_dialog):
        format_dialog.high_def_button_2.setText('Low Quality')
        for i in reversed(range(gridLayout_5.count())): 
            gridLayout_5.itemAt(i).widget().setParent(None)
        for i in reversed(range(gridLayout_6.count())): 
            gridLayout_6.itemAt(i).widget().setParent(None)
        for i in reversed(range(gridLayout_7.count())): 
            gridLayout_7.itemAt(i).widget().setParent(None)

        try :
            stream = yt.streams.filter(only_audio=True)
            res = []
            for audio in stream:
                res.append(audio.resolution)

            if '1080p' not in res:
                format_dialog.gridLayout.removeWidget(format_dialog.high_def_button)
                format_dialog.label_7 = None

            else:
                if format_dialog.high_def_button.isChecked:
                    music = stream.filter(resolution='1080p').first()
                    filesize = music.filesize
                    format_dialog.label_7.setText(size(filesize, system=alternative)) 
                    format_dialog.label_5.setText(music.resolution)

            if '1080p' not in res:
                format_dialog.gridLayout_4.removeWidget(format_dialog.high_def_button_2)
                format_dialog.label_7 = None

            else:
                if format_dialog.high_def_button.isChecked:
                    music = stream.filter(resolution='1080p').first()
                    filesize = music.filesize
                    format_dialog.label_9.setText(size(filesize, system=alternative))  
                    format_dialog.label_8.setText(music.resolution)
            format_dialog.show() 
        except Exception as e:
            raise e 

    def dowload_video(self, yt, format_dialog:FormatDialog):
        try : 
            stream = yt.streams.filter(progressive=True)
            stream = stream.filter(file_extension='mp4')
            print(stream)
            res = []
            for video in stream:
                res.append(video.resolution)

            if '1080p' not in res:
                format_dialog.high_def_button.setCheckable(False)
                format_dialog.label_7 = None
            else:
                music = stream.filter(resolution='1080p').first()
                filesize = music.filesize
                format_dialog.label_7.setText(size(filesize, system=alternative))
                if format_dialog.high_def_button.isChecked:
                    self.for_download = music

            if '720p' not in res:
                format_dialog.high_def_button_2.setCheckable(False)
                format_dialog.label_9 = None
            else:
                music = stream.filter(resolution='720p').first()
                filesize = music.filesize
                format_dialog.label_9.setText(size(filesize, system=alternative))
                if format_dialog.high_def_button_2.isChecked:
                    self.for_download = music

            if '480p' not in res:
                format_dialog.high_def_button_3.setCheckable(False)
                format_dialog.label_12 = None
            else:
                music = stream.filter(resolution='480p').first()
                filesize = music.filesize
                format_dialog.label_12.setText(size(filesize, system=alternative))
                if format_dialog.high_def_button_3.isChecked:
                    self.for_download = music

            if '360p' not in res:
                format_dialog.high_def_button_4.setCheckable(False)
                format_dialog.label_16 = None
            else:
                music = stream.filter(resolution='360p').first()
                filesize = music.filesize
                format_dialog.label_16.setText(size(filesize, system=alternative))
                if format_dialog.high_def_button_4.isChecked:
                    self.for_download = music

            if '240p' not in res:
                format_dialog.high_def_button_5.setCheckable(False)
                format_dialog.label_17 = None
            else:
                music = stream.filter(resolution='240p').first()
                filesize = music.filesize
                format_dialog.label_17.setText(size(filesize, system=alternative))
                if format_dialog.high_def_button_5.isChecked:
                    self.for_download = music

            if '144p' not in res:
                format_dialog.high_def_button_6.setCheckable(False)
                format_dialog.label_19 = None
            else:
                music = stream.filter(resolution='144p').first()
                filesize = music.filesize
                format_dialog.label_19.setText(size(filesize, system=alternative))
                if format_dialog.high_def_button_6.isChecked:
                    self.for_download = music

            format_dialog.show()

        except Exception as e:
            raise e 
    
    def load_data(self):
        pass


def main(args):
        app =QApplication(args)
        window = MainWindow()
        window.show()
        frame = app.exec_()
        return frame

if __name__=="__main__":
    main(sys.argv)

