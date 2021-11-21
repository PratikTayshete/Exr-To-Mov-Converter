import sys
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2 import QtCore
from gui.converterUI import Ui_Converter
from lib import converter
from utils import tools, constants


class ConverterWindow(QMainWindow, Ui_Converter):
    def __init__(self):
        super(ConverterWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint |
            QtCore.Qt.WindowCloseButtonHint
        )
        self.dialogs = tools.Dialogs()
        self.check_env()
        self.is_exr_folder_valid = False
        self.converter = converter.Converter()
        self.connect_widgets()

    def check_env(self):
        """
        Checks if required parameters is added as environment variable.
        """
        if constants.FFMPEG_EXECUTABLE is None:
            message = """
            Add FFMPEG executable file path in your environment
            eg: FFMPEG_EXECUTABLE=Path/to/the/file/ffmpeg.exe
            """
            self.dialogs.message_dialog("FFMPEG WARNING!!", message)
            self.close()
        else:
            self.show()

    def connect_widgets(self):
        """
        Connect the signals generated from the widgets with their
        functionalities.
        """
        self.browse_exr_folder_pushButton.clicked.connect(
            self.select_exr_folder
        )
        self.browse_output_folder_pushButton.clicked.connect(
            self.select_output_folder
        )
        self.convert_pushButton.clicked.connect(self.convert_images)

    def select_exr_folder(self):
        """
        Select the directory where exr image sequences are saved.
        """
        self.exr_folder_path_lineEdit.clear()
        exr_directory = self.dialogs.file_dialog()
        if exr_directory != "":
            is_dir_valid = self.converter.check_exr_files(
                dir_path=exr_directory
            )
            if not is_dir_valid:
                self.is_exr_folder_valid = False
                message = "Please select a folder that contains only exr " \
                          "image sequences"
                self.dialogs.message_dialog(
                    "Invalid EXR Folder", message
                 )
            else:
                self.exr_folder_path_lineEdit.setText(exr_directory)
                self.is_exr_folder_valid = True

        else:
            self.exr_folder_path_lineEdit.clear()

    def select_output_folder(self):
        """
        Select the directory where the output mov will be saved.
        """
        self.output_folder_path_lineEdit.clear()
        output_directory = self.dialogs.file_dialog()
        if output_directory == "":
            self.output_folder_path_lineEdit.clear()
        else:
            self.output_folder_path_lineEdit.setText(output_directory)

    def convert_images(self):
        """
        Converts the exr image sequences into an mov file.
        """
        are_paths_valid = self.validate_paths()
        if are_paths_valid:
            input_dir = self.exr_folder_path_lineEdit.text()
            output_dir = self.output_folder_path_lineEdit.text()
            self.progressBar.setValue(50)
            conversion_params = self.converter.convert_exr_mov(
                input_dir=input_dir,
                output_dir=output_dir
            )
            self.progressBar.setValue(100)
            if conversion_params.get("status"):
                message = f"""
                {conversion_params.get("output_path")}
                File Size: {conversion_params.get("file_size")}
                """
                self.dialogs.message_dialog("Conversion Successful", message)
                self.progressBar.setValue(0)
                self.exr_folder_path_lineEdit.clear()
                self.output_folder_path_lineEdit.clear()
            else:
                message = "Some error occurred in the conversion process."
                self.dialogs.message_dialog("Conversion Failed", message)
                self.progressBar.setValue(0)
                self.exr_folder_path_lineEdit.clear()
                self.output_folder_path_lineEdit.clear()

    def validate_paths(self):
        """
        Validates both the exr images directory and the output directory

        :return is_valid: True if both the exr images directory and
        output directory paths are valid.
        :rtype: bool
        """
        is_valid = False
        input_dir = self.exr_folder_path_lineEdit.text()
        output_dir = self.output_folder_path_lineEdit.text()
        # Check for empty paths.
        if input_dir == "":
            self.dialogs.message_dialog(
                "EXR Images Path",
                "Please select a folder with exr image sequences."
            )
            return is_valid
        if output_dir == "":
            self.dialogs.message_dialog(
                "Output Path",
                "Please select a folder for the output mov file."
            )
            return is_valid
        if self.is_exr_folder_valid:
            is_valid = True
        return is_valid


if __name__ == '__main__':
    app = QApplication()
    converter_window = ConverterWindow()
    sys.exit(app.exec_())
