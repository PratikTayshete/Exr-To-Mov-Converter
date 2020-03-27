import re
import os
import subprocess
from PySide2.QtWidgets import QFileDialog


def get_frame_number_and_path(single_exr_file_path):
    """
    This function takes the absolute path of a single exr file and returns the start number and input path required for conversion.

    :param single_exr_file_path: The absolute path to the first exr file from the multiple exr sequences.

    :returns:
    start_number: The starting number of the frame among the multiple exr sequences.
    new_file_path_with_padding_suffix: The absolute file path padded till the specific length.
    """
    original_file_path = single_exr_file_path
    # Extract the start number from the frame
    pattern = re.compile(r'\d+\.exr$')
    number_result = pattern.findall(original_file_path)
    start_number = number_result[0].split(".")[0]
    # Create the input file name with appropriate suffix (padding)
    padding_number = len(list(start_number))
    padding_suffix = "%" + str(padding_number) + "d.exr"
    file_name_result = pattern.finditer(original_file_path)
    replace_index = [replace_start_index.start() for replace_start_index in file_name_result]
    new_file_path_with_padding_suffix = original_file_path[:replace_index[0]] + padding_suffix
    return start_number, new_file_path_with_padding_suffix


def check_exr_files(exr_folder_path):
    """
    This function checks whether all the files in the given directory are of type [.exr].

    :param exr_folder_path: The absolute path to the directory where exr sequences are stored.

    :return: exr_file_flag: Returns True if all files have the extenstion of .exr else returns False.
    """
    exr_file_flag = None
    all_file_names_in_exr_folder = os.listdir(exr_folder_path)
    exr_suffix_pattern = re.compile(r'\.exr$')
    for file_name in all_file_names_in_exr_folder:
        search_result = exr_suffix_pattern.search(file_name)
        if search_result:
            exr_file_flag = True
        else:
            exr_file_flag = False
            break
    return exr_file_flag


def file_open_dialog():
    """
    This function opens a FileDialog box to browse and select a file directory.
    """
    return QFileDialog.getExistingDirectory(options=QFileDialog.DontUseNativeDialog)


def get_video_size(abs_video_path, size_unit=0):
    """
    This function takes the absolute path of the video file and returns its size with appropriate notation for the unit.

    :param abs_video_path:  The absolute path of the video file.
    :param size_unit: Value to indicate the unit to be displayed.

    :return: Memory size with specific notation.
    """
    kb = 1
    mb = 2
    gb = 3
    if size_unit == kb:
        return "{:.2f}".format(os.path.getsize(abs_video_path) * 0.001), "KB"
    elif size_unit == mb:
        return "{:.2f}".format(os.path.getsize(abs_video_path) * 0.000001), "MB"
    elif size_unit == gb:
        return "{:.4f}".format(os.path.getsize(abs_video_path) * 0.000000001), "GB"
    else:
        return os.path.getsize(abs_video_path), "bytes"


def get_video_duration(abs_video_path):
    """
    This function takes the absolute path of a video file and returns the duration of the video file in specific format.

    :param abs_video_path: The absolute path of the video file.

    :return: video_duration: The duration of the video in H:MM:SS format.
    """
    video_duration_data = subprocess.check_output(
        ['ffprobe', '-i', abs_video_path, '-v', 'quiet', '-sexagesimal', '-print_format',
         'compact=print_section=0:nokey=1:escape=csv', '-show_entries', 'format=duration'])
    video_duration = str(video_duration_data, encoding="utf-8").split('.')[0]
    return video_duration
