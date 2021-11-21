from PySide2.QtWidgets import QFileDialog, QMessageBox
from gui import stylesheet


class Dialogs:
    @staticmethod
    def file_dialog():
        """
        Opens a FileDialog box to browse and select a file directory.

        :return: file_dialog: A file dialog instance to browse directory.
        :rtype: QFileDialog
        """
        file_dialog = QFileDialog.getExistingDirectory(
            options=QFileDialog.DontUseNativeDialog
        )
        return file_dialog

    @staticmethod
    def message_dialog(title, message):
        """
        Opens a MessageBox dialog to display a message with a title.

        :param str title: Title for the message dialog.
        :param str message: Message to be displayed in the message
        dialog.
        :return:
        """
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.setStyleSheet(stylesheet.MESSAGE_BOX_STYLESHEET)
        display_message = message_box.exec_()
        return display_message
