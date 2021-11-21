import re
import os
import shlex
import subprocess
from utils import constants


class Converter:
    @staticmethod
    def get_frame_number_and_path(file_path):
        """
        Takes the absolute file path of a single exr file and returns
        the information about the exr frames sequence.

        :param str file_path: The absolute path to the first exr file
        from the multiple exr sequences.
        :return frames_info: Information about the exr frames required
        for conversion process.
        :rtype: dict
        """
        # Extract the start number from the frame
        pattern = re.compile(r'\d+\.exr$')
        number_result = pattern.findall(file_path)
        start_number = number_result[0].split(".")[0]
        # Create the input file name with appropriate suffix (padding)
        padding_number = len(list(start_number))
        padding_suffix = "%" + str(padding_number) + "d.exr"
        file_name_result = pattern.finditer(file_path)
        replace_index = [
            start_index.start() for start_index in file_name_result
        ]
        padded_file_path = file_path[:replace_index[0]] + padding_suffix
        frames_info = {
            "padded_file_path": padded_file_path,
            "start_frame_number": start_number
        }
        return frames_info

    @staticmethod
    def check_exr_files(dir_path):
        """
        Checks whether all the files in the given directory are of type
        [.exr].

        :param str dir_path: The absolute path to the directory where
        exr sequences are stored.
        :return: exr_file_flag: Returns True if all files have the
        extension of .exr else returns False.
        :rtype: bool
        """
        exr_file_flag = False
        file_names = os.listdir(dir_path)
        exr_suffix_pattern = re.compile(r'\.exr$')
        for file_name in file_names:
            search_result = exr_suffix_pattern.search(file_name)
            if search_result:
                exr_file_flag = True
            else:
                break
        return exr_file_flag

    @staticmethod
    def get_video_size(file_path, unit="KB"):
        """
        Takes the absolute path of the video file and returns its size
        with appropriate notation for the unit.

        :param str file_path:  The absolute path of the video file.
        :param str unit: Value to indicate the unit to be displayed.
        Default value is 'KB'
        :return: video_size: Size of the video file with notation.
        :rtype: str
        """
        size_units = {
            "KB": [1, 0.001],
            "MB": [2, 0.000001],
            "GB": [3, 0.000000001]
        }
        video_size = os.path.getsize(file_path) * size_units[unit][1]
        video_size = "{:.2f} {}".format(video_size, unit)
        return video_size

    def convert_exr_mov(self, input_dir, output_dir):
        """
        Converts the exr image sequences into mov and saves it to the
        given output directory.

        :param str input_dir: Absolute path of the directory where exr
        image sequences are saved.
        :param str output_dir: Absolute path of the directory where the
        converted mov file will be saved.
        :return: conversion_params: Parameters of the conversion process.
        :rtype: dict
        """
        conversion_status = False
        output_file_name = "output.mov"
        output_file_path = os.path.join(output_dir, output_file_name)
        output_file_path = output_file_path.replace("\\", "/")
        exr_files = sorted(os.listdir(input_dir))
        exr_file_path = os.path.join(input_dir, exr_files[0])
        exr_file_path = exr_file_path.replace("\\", "/")
        frames_info = self.get_frame_number_and_path(file_path=exr_file_path)
        frame_number = frames_info.get("start_frame_number")
        padded_path = frames_info.get("padded_file_path")
        ffmpeg_exe = constants.FFMPEG_EXECUTABLE.replace("\\", "/")
        conversion_command = "{} -hide_banner " \
                             "-loglevel quiet -y -start_number " \
                             "{} -i {} -vcodec " \
                             "mpeg4 {}".format(
                                ffmpeg_exe,
                                frame_number,
                                padded_path,
                                output_file_path
                                )
        return_code = subprocess.call(shlex.split(conversion_command))
        if return_code == 0:
            conversion_status = True
            conversion_params = {
                "status": conversion_status,
                "output_path": output_file_path,
                "file_size": self.get_video_size(output_file_path, "MB")
            }
        else:
            conversion_params = {
                "status": conversion_status
            }
        return conversion_params

