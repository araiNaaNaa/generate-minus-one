import os
import inspect
from spleeter.separator import Separator


class Extractor:
    already = False

    def __init__(self):
        print('Extractor.__init__')

    def main(self, alredy_add_path, mp3_file_path, dest_folder_name):
        print(' ****************************************')
        print(' Start : Separate music file')
        print(' ****************************************')

        if not 'ffmpegmaster' in os.environ['PATH']:
            parent_dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

            bin_path = os.path.join(parent_dir_path + '\\ffmpegmaster\\', 'bin')
            os.environ['PATH'] = '{};{}'.format(bin_path, os.environ['PATH'])  # セミコロン付きでPATHの先頭に追加

        print('File path：', mp3_file_path)
        separator = Separator('spleeter:4stems')

        print('execute')
        separator.separate_to_file(mp3_file_path, dest_folder_name)

        print(' ****************************************')