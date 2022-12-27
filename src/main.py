import PySimpleGUI as sg
import os
import re
import sys
import time
import shutil
from mixer import Mixer
from extractor import Extractor
from downloader import DownloadFromYoutube

# from multiprocessing.pool import ThreadPool
from const.download_consts import DownloadCodec
from high_pitch_harmonic_extractor import HighPitchHarmonicExtractor

COLOR_MAP = {
    'black': '#000000',
    'white': '#FFFFFF',
    'gray': '#D3D3D3',
    'blue': '#1874CD'
}

# ffmpegNormalize = ffmpeg_normalize.FFmpegNormalize()
# mixer = Mixer()
# extractor = Extractor()
# downloadFromYoutube = DownloadFromYoutube()
# highPitchHarmonicExtractor = HighPitchHarmonicExtractor()

# pool = ThreadPool(processes=1)
code_regex = re.compile('[!"#$%&\'\\\\*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・＄＃＠。、？！｀＋￥％]')

class OpenWindow:

    KEY_YOUTUBE_URL_BUTTON = 'fromYoutube'
    KEY_FROM_LOCAL_BUTTON = 'fromLocal'
    KEY_EXPORT_BUTTON = 'export_button'

    KEY_LABEL_VO = 'Vocal'
    KEY_LABEL_GT = "Other(Guitar)"
    KEY_LABEL_BA = 'Bass'
    KEY_LABEL_PF = 'Piano'
    KEY_LABEL_DR = 'Drums'

    IS_ALREADY_ADD_FFMPEG_PATH = False
    sg.theme('Reddit')  # デザインテーマの設定

    radio_dic = {
        '-1-': 'aaa',
        '-2-': 'bbb',
        '-3-': 'ccc',
    }
    # [sg.Radio(item[1], key=item[0], group_id='0') for item in radio_dic.items()],
#    layout_codec_radio = [
#        [sg.Text('ハードな曲をダウンロードする時、または、高音質でダウンロードしたけど微妙な時', key='456')],
#        [sg.Radio(DownloadCodec.FLAC.codec, group_id='dl_codec_radio', default=True, key='-FLAC-'),
#        sg.Radio(DownloadCodec.WAV.codec, group_id='dl_codec_radio', key='-WAV-'),
#        sg.Radio(DownloadCodec.MP3.codec, group_id='dl_codec_radio', key='-MP3-')],
#    ]

    codec_frame_layout = [
        [
            sg.Checkbox(DownloadCodec.FLAC.codec, key=DownloadCodec.FLAC.codec, default=True, disabled=True),
            sg.Checkbox(DownloadCodec.WAV.codec, key=DownloadCodec.WAV.codec, default=False),
            sg.Checkbox(DownloadCodec.MP3.codec, key=DownloadCodec.MP3.codec, default=False),
            sg.Checkbox(DownloadCodec.M4A.codec, key=DownloadCodec.M4A.codec, default=False),

            sg.Checkbox(DownloadCodec.ALAC.codec, key=DownloadCodec.ALAC.codec, default=False, visible=False),
            sg.Checkbox(DownloadCodec.AIFF.codec, key=DownloadCodec.AIFF.codec, default=False, visible=False),
            sg.Checkbox(DownloadCodec.OPUS.codec, key=DownloadCodec.OPUS.codec, default=False, visible=False),
            sg.Checkbox(DownloadCodec.VORBIS.codec, key=DownloadCodec.VORBIS.codec, default=False, visible=False),
            sg.Checkbox(DownloadCodec.AAC.codec, key=DownloadCodec.AAC.codec, default=False, visible=False),
            sg.Checkbox(DownloadCodec.MP4A.codec, key=DownloadCodec.MP4A.codec, default=False, visible=False),
        ]
    ]
    download_codec_frame_layout = [
        [
            sg.Checkbox(DownloadCodec.FLAC.codec, key='dl_codec_flac', default=True, disabled=True),
            sg.Checkbox(DownloadCodec.WAV.codec, key='dl_codec_wav', default=False),
            sg.Checkbox(DownloadCodec.MP3.codec, key='dl_codec_mp3', default=False),
        ]
    ]
    inst_frame_layout = [
        [
            sg.Checkbox("Vocal", key='vo', default=True),
            sg.Checkbox("Other(Guitar)", key='gt', default=True),
            sg.Checkbox("Bass", key='ba', default=True),
            # sg.Checkbox("Piano", key='pf', default=False, disabled=True),
            sg.Checkbox("Drums", key='dr', default=False)
        ],
        [
            sg.Checkbox("高音の補正", key='add_high', default=False),
        ]
    ]

    layout_input = [

        [
            sg.Text('Youtube', size=(10, 1), key='fromText'),
            sg.Input(key='path', disabled=False),
            sg.FileBrowse('ファイルを選択', key='fileSelectBrowse', visible=False),
            sg.Button('    決定    ', key='fileSpecified', visible=False),
            sg.Button('  ダウンロード  ', key='downloadFromYoutube', visible=True),
        ],
        # [
        #     [sg.Text('ハードな曲をダウンロードする時、または、高音質でダウンロードしたけど微妙な時', key='123')],
        #     [sg.Radio(DownloadCodec.FLAC.codec, group_id='dl_codec_radio', default=True, key='-FLAC-')],
        #     [sg.Radio(DownloadCodec.WAV.codec, group_id='dl_codec_radio', key='-WAV-')],
        #     [sg.Radio(DownloadCodec.MP3.codec, group_id='dl_codec_radio', key='-MP#-')],
        # ],
        # [
        #     sg.Frame(title="ファイル形式", key='srcCodecRadio', layout=layout_codec_radio, border_width=1)
        # ],
        [
            sg.Frame(title="ファイル形式(FLACは固定)", key='downloadFileCodec', layout=codec_frame_layout, border_width=1)
        ],
    ]

    layout_target = [
        [
            sg.Text('ファイル名'),
            sg.Input('test', key='mp3FileName', disabled=True),
        ],
        [
            sg.Text('ファイルパス'),
            sg.Input('default', key='mp3FilePath', visible=True)
        ],
    ]

    layout = [
        [
            sg.Button(
                "Youtube",
                key=KEY_YOUTUBE_URL_BUTTON,
                disabled=True,
                disabled_button_color=(COLOR_MAP['black'], COLOR_MAP['blue'])
            ),
            sg.Button(
                "ローカル",
                key=KEY_FROM_LOCAL_BUTTON,
                disabled=False,
                disabled_button_color=(COLOR_MAP['black'], COLOR_MAP['blue'])
            )
        ],
        [
            sg.Frame(title="曲を選択", layout=layout_input, border_width=3, key="selectMusic"),
        ],
        [
            sg.Frame(title="対象ファイル", layout=layout_target, border_width=3),
        ],
        [
            sg.Frame(title="出力ファイルに含める楽器を選択", layout=inst_frame_layout, border_width=3),
            sg.Button('    抽出    ', key=KEY_EXPORT_BUTTON, disabled=True),
        ],
        [
            # sg.Button('OK'),
            sg.Button('閉じる')
        ],
        # [sg.Output(size=(80, 20))],

    ]

    codec_extension = '.flac'

    # Generate Window
    window = sg.Window('Minus One Extractor', layout)
    # window = sg.Window('Minus One Extractor', layout, resizable=True, finalize=True)
    # window["selectMusic"].expand(expand_x=True, expand_y=True)

    def update_disabled(self, keys):
        for key in keys:
            self.window.find_element(key).Update(disabled=True)

    def update_enabled(self, keys):
        for key in keys:
            self.window.find_element(key).Update(disabled=False)

    def main(self):
        print('main.main')
        # try:
            # Event loop
        while True:
            try:
                event, values = self.window.read()

                if event == sg.WIN_CLOSED or event == 'キャンセル':
                    break
                elif event == 'OK':
                    print(values)
                elif event == self.KEY_YOUTUBE_URL_BUTTON:
                    # mp3FileName
                    self.update_enabled([self.KEY_FROM_LOCAL_BUTTON,
                                         'downloadFromYoutube'])

                    self.update_disabled([self.KEY_YOUTUBE_URL_BUTTON,
                                          'fileSelectBrowse', self.KEY_EXPORT_BUTTON])

                    self.window.find_element('path').Update('')
                    self.window.find_element('mp3FilePath').Update('')
                    self.window.find_element('fromText').Update('Youtube')
                    self.window.find_element('downloadFileCodec').Update(visible=True)
                    # self.window.find_element('src_file_codec').Update(visible=True)
                    self.window.find_element('fileSelectBrowse').Update(visible=False)
                    self.window.find_element('downloadFromYoutube').Update(visible=True)
                    self.window.find_element('fileSpecified').Update(visible=False)

                elif event == self.KEY_FROM_LOCAL_BUTTON:
                    self.window.find_element('downloadFromYoutube').Update(visible=False)
                    self.window.find_element('fileSelectBrowse').Update(visible=True)
                    self.window.find_element('fileSpecified').Update(visible=True)

                    self.update_enabled([self.KEY_YOUTUBE_URL_BUTTON, 'fileSpecified', 'fileSelectBrowse'])
                    self.update_disabled([self.KEY_FROM_LOCAL_BUTTON, 'downloadFromYoutube',
                                          self.KEY_EXPORT_BUTTON])

                    self.window.find_element('path').Update('')
                    self.window.find_element('mp3FilePath').Update('')
                    self.window.find_element('fromText').Update('ローカル')
                    self.window.find_element('downloadFileCodec').Update(visible=False)
                    # self.window.find_element('src_file_codec').Update(visible=False)

                elif event == 'downloadFromYoutube':
                    if values['path'] is None or '' == str(values['path']):
                        print('未入力 / 未指定')
                    else:

                        codecs = [DownloadCodec.FLAC]

                        if values[DownloadCodec.WAV.codec]:
                            codecs.append(DownloadCodec.WAV)
                        if values[DownloadCodec.MP3.codec]:
                            codecs.append(DownloadCodec.MP3)

                        if values[DownloadCodec.M4A.codec]:
                            codecs.append(DownloadCodec.M4A)

                        if values[DownloadCodec.WAV.codec]:
                            codecs.append(DownloadCodec.WAV)

                        if values[DownloadCodec.ALAC.codec]:
                            codecs.append(DownloadCodec.FLAC)

                        if values[DownloadCodec.AIFF.codec]:
                            codecs.append(DownloadCodec.AIFF)

                        if values[DownloadCodec.OPUS.codec]:
                            codecs.append(DownloadCodec.OPUS)

                        if values[DownloadCodec.VORBIS.codec]:
                            codecs.append(DownloadCodec.VORBIS)

                        if values[DownloadCodec.AAC.codec]:
                            codecs.append(DownloadCodec.AAC)

                        if values[DownloadCodec.MP4A.codec]:
                            codecs.append(DownloadCodec.MP4A)

#                        if values['-FLAC-']:
#                            self.codec_extension = '.flac'
#                            if DownloadCodec.FLAC not in codecs:
#                                codecs.append(DownloadCodec.FLAC)
#
#                        elif values['-WAV-']:
#                            self.codec_extension = '.wav'
#                            if DownloadCodec.WAV not in codecs:
#                                codecs.append(DownloadCodec.WAV)
#                        elif values['-MP3-']:
#                            self.codec_extension = '.mp3'
#                            if DownloadCodec.MP3 not in codecs:
#                                codecs.append(DownloadCodec.MP3)
                        parent_dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
                        uploaded_file_name = DownloadFromYoutube().main(values['path'], codecs)

                        time.sleep(3)

                        title = code_regex.sub('', uploaded_file_name)
                        os.rename(parent_dir_path + '\\music\\' + uploaded_file_name + '\\' + uploaded_file_name + self.codec_extension,
                                  parent_dir_path + '\\music\\' + uploaded_file_name + '\\' + title + self.codec_extension)

                        os.rename(parent_dir_path + '\\music\\' + uploaded_file_name,
                                  parent_dir_path + '\\music\\' + title)

                        self.window.find_element(self.KEY_EXPORT_BUTTON).Update(disabled=False)
                        self.window.find_element('mp3FileName').Update(title)

                        music_file_path = parent_dir_path + '\\music\\' + title + '\\' + title + self.codec_extension

                        self.window.find_element('mp3FilePath').Update(music_file_path)

                        print(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

                elif event == 'fileSpecified':
                    if values['path'] is None or '' == str(values['path']):
                        print('未入力 / 未指定')
                    elif not (str(values['path']).endswith('.mp3')
                              or str(values['path']).endswith('.wav')
                              or str(values['path']).endswith('.flac')):
                        print('現在はインプットは[MP3 / wav / flac]のみ対応')
                    else:
                        print('path=', values['path'])
                        self.window.find_element('mp3FilePath').Update(values['path'])

                        # Generate folder name from music file path

                        music_file_name = os.path.split(os.path.basename(values['path']))[1]

                        self.codec_extension = os.path.splitext(values['path'])[1]
                        folder_name = music_file_name.replace(self.codec_extension, '')

                        # split_path = values['path'].split('\\')
                        # music_file_name = split_path[len(split_path) - 1]
                        # print(split_path)
                        # split_path(music_file_name)

                        # print('music_file_name:', os.path.splitext(os.path.basename(music_file_name))[0])
                        # # filename.tar
                        # if str(values['path']).endswith('.mp3'):
                        #     folder_name = music_file_name.replace('.mp3', '')
                        #     self.codec_extension = '.mp3'
                        #
                        # elif str(values['path']).endswith('.wav'):
                        #     folder_name = music_file_name.replace('.wav', '')
                        #     self.codec_extension = '.wav'
                        #
                        # elif str(values['path']).endswith('.flac'):
                        #     folder_name = music_file_name.replace('.flac', '')
                        #     self.codec_extension = '.flac'

                        print('path=', values['path'])
                        print('mp3FilePath=', values['mp3FilePath'])
                        print('folder_name=', folder_name)
                        print('music_file_name=', music_file_name)
                        print('self.codec_extension=', self.codec_extension)

                        if not os.path.exists('..\\music\\' + folder_name):
                            os.mkdir('..\\music\\' + folder_name)

                        if not os.path.exists('..\\download\\' + folder_name + '\\' + music_file_name):
                            shutil.copyfile(values['path'], '..\\music\\' + folder_name + '\\' + music_file_name)

                        self.window.find_element('mp3FileName').Update(music_file_name)
                        self.window.find_element(self.KEY_EXPORT_BUTTON).Update(disabled=False)

                elif event == self.KEY_EXPORT_BUTTON:
                    print(self.KEY_EXPORT_BUTTON)

                    try:
                        dest_folder_name = '..\\music\\'
                        Extractor().main(self.IS_ALREADY_ADD_FFMPEG_PATH, values['mp3FilePath'], dest_folder_name)
                        self.IS_ALREADY_ADD_FFMPEG_PATH = True

                    except Exception as e:
                        print('error')
                        print(e)
                        continue

                    music_file_name = os.path.split(os.path.basename(values['mp3FilePath']))[1]
                    folder_name = music_file_name.replace(self.codec_extension, '')

                    if values['add_high']:
                        HighPitchHarmonicExtractor().generate('..\\music\\' + music_file_name, music_file_name)

                    # FIXME pfを消す
                    Mixer().main(folder_name, values['vo'],
                               values['gt'], values['ba'], values['dr'], False, values['add_high'])
                               # values['gt'], values['ba'], values['dr'], values['pf'], values['add_high'])

            except Exception as err:
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print('!!           エラー          !!')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(err)
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print ("%s, %s, %s" % (exc_type, fname, exc_tb.tb_lineno))
                continue
        self.window.close()

        # except Exception as e:
        #     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        #     print(e)
        #     return

        def close():
            self.window.close()


openWindow = OpenWindow()

if __name__ == '__main__':
    openWindow.main()
    # openWindow.test()

