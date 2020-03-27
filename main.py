import sys
import os
import subprocess
from PySide2.QtWidgets import (QApplication, QMainWindow)
from gui.converterUI import Ui_MainAppWindow
from utils import converter_utils


class MainAppWindow(QMainWindow, Ui_MainAppWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainAppWindow.__init__(self)
        self.setupUi(self)
        self.movFolderButton.setDisabled(True)
        self.conversionButton.setDisabled(True)
        self.mov_folder_path = ""
        self.exr_folder_path = ""
        self.exrFolderButton.clicked.connect(self.open_exr_folder)
        self.movFolderButton.clicked.connect(self.open_mov_folder)
        self.conversionButton.clicked.connect(self.convert_exr_to_mov)

    def convert_exr_to_mov(self):
        """
        Converts the exr sequences to a mov file.
        """
        self.conversionLogTextEdit.appendPlainText("Converting......")
        converted_video_name = "mov_converted"
        converted_video_extension = ".mov"
        abs_mov_file_path = os.path.join(self.mov_folder_path, converted_video_name + converted_video_extension)
        # Get the first file name of the exr sequences
        single_exr_file_path = sorted(os.listdir(self.exr_folder_path))[0]
        abs_single_exr_file_path = os.path.join(self.exr_folder_path, single_exr_file_path)
        start_frame_number, abs_path_with_padding = converter_utils.get_frame_number_and_path(abs_single_exr_file_path)
        return_code = subprocess.call(
            ['ffmpeg', '-hide_banner', '-loglevel', 'quiet', '-y', '-start_number', start_frame_number, '-i',
             abs_path_with_padding, '-vcodec', 'mpeg4', abs_mov_file_path])

        if return_code != 0:
            self.conversionLogTextEdit.appendPlainText("\nSome error occured while conversion")
        else:
            if os.path.isfile(abs_mov_file_path):
                self.conversionLogTextEdit.appendPlainText("\nConversion completed successfully..")
                self.conversionLogTextEdit.appendPlainText("\n\n----MOV File Details:----")
                self.conversionLogTextEdit.appendPlainText("File Path:\t{}".format(abs_mov_file_path))
                video_file_size = converter_utils.get_video_size(abs_mov_file_path, 2)
                self.conversionLogTextEdit.appendPlainText(
                    "File Size:\t{} {}".format(video_file_size[0], video_file_size[1]))
                self.conversionLogTextEdit.appendPlainText("File Duration:\t{}".format(converter_utils.get_video_duration(abs_mov_file_path)))

    def open_mov_folder(self):
        """
        Reads the path to the directory where MOV file is to be saved after conversion.
        """
        self.mov_folder_path = converter_utils.file_open_dialog()
        mov_message_header = "----MOV Directory----"
        if not self.mov_folder_path:
            self.conversionLogTextEdit.appendPlainText(
                mov_message_header + "\n" + "Please select a destination directory for MOV file.")
        else:
            self.conversionLogTextEdit.appendPlainText(
                mov_message_header + "\n\n" + "Current MOV directory selected:\t" + self.mov_folder_path)
            self.conversionButton.setEnabled(True)

    def open_exr_folder(self):
        """
        Reads the path to the directory where the EXR sequences are stored.
        """
        self.conversionLogTextEdit.clear()
        self.exr_folder_path = converter_utils.file_open_dialog()
        if not self.exr_folder_path:
            self.conversionLogTextEdit.clear()
            self.conversionLogTextEdit.setPlainText("Please select an exr sequence directory")
        else:
            all_exr_files_flag = converter_utils.check_exr_files(self.exr_folder_path)
            exr_message_header = "----EXR Sequences----"
            if all_exr_files_flag:
                self.movFolderButton.setEnabled(True)
                total_exr_files = len(os.listdir(self.exr_folder_path))
                exr_folder_message = exr_message_header + "\n\nEXR sequences folder selected:\t" + self.exr_folder_path + "\n\nTotal EXR files detected:\t" + str(
                    total_exr_files)
                self.conversionLogTextEdit.setPlainText(exr_folder_message)

            else:
                exr_folder_message = exr_message_header + "\n\nWrong file type detected. Please check the path and try " \
                                                          "again. "
                self.conversionLogTextEdit.setPlainText(exr_folder_message)


if __name__ == '__main__':
    app = QApplication()
    mainAppWindow = MainAppWindow()
    mainAppWindow.show()
    sys.exit(app.exec_())
