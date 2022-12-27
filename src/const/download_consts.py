from enum import Enum

outtmpl = '../music/' + "%(title)s/" + "%(title)s" + '.%(ext)s'

ydl_opts_flac = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'outtmpl': outtmpl,
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'flac'},
        {'key': 'FFmpegMetadata'},
        {'key': 'EmbedThumbnail'},
    ],
}

ydl_opts_wav = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'outtmpl': outtmpl,
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'},
        {'key': 'FFmpegMetadata'},
        {'key': 'EmbedThumbnail'},
    ],
}

ydl_opts_mp3 = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'outtmpl': outtmpl,
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'},
        {'key': 'FFmpegMetadata'},
        {'key': 'EmbedThumbnail'},
    ],
}

ydl_opts_m4a = {
    'writethumbnail': True,
    'format': 'm4a/bestaudio/best',
    'outtmpl': outtmpl,
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a'},
        {'key': 'FFmpegMetadata'},
        {'key': 'EmbedThumbnail'},
    ],
}
# class DownloadCodec(Enum):
#
#     RED = (1, '赤', '1', ydl_opts_mp3)
#     GREEN = (2, '緑', '2', ydl_opts_mp3)
#     BLUE = (3, '青', '3', ydl_opts_mp3)
#
#     def __init__(self, id, type, ex1, opt):
#         self.id = id
#         self.type = type
#         self.ex1 = ex1
#         self.opt = opt


class DownloadCodec(Enum):
    FLAC = (0, 'FLAC', '.flac', ydl_opts_flac)
    WAV = (1, 'WAV', '.wav', ydl_opts_wav)
    MP3 = (2, 'MP3', '.mp3', ydl_opts_mp3)
    M4A = (3, 'M4A', 'm4a', ydl_opts_m4a)

    # Not Supported
    ALAC = (4, 'ALAC', '.alac', ydl_opts_mp3)
    AIFF = (5, 'AIFF', '.aiff', ydl_opts_mp3)
    OPUS = (6, 'OPUS', '.opus', ydl_opts_mp3)
    VORBIS = (7, 'VORBIS', '.vorbis', ydl_opts_mp3)
    AAC = (8, 'AAC', '.aac', ydl_opts_mp3)
    MP4A = (9, 'MP4A', '.mp4a', ydl_opts_mp3)

    # def __init__(self, id, codec, extension, opt):
    #     self.id = id
    #     self.codec = codec
    #     self.extension = extension
    #     self.opt = opt
    def __init__(self, id, codec, extension, opt):
        self.id = id
        self.codec = codec
        self.extension = extension
        self.opt = opt

    # 全メンバーを取得する
    @classmethod
    def members_as_list(cls):
        # Order dictionary -> list
        return [*cls.__members__.values()]

    # idを指定して取得する
    @classmethod
    def get_by_id(cls, id):
        for c in cls.members_as_list():
            if id == c.id:
                return c
        # default
        return DownloadCodec.FLAC

    def get_opts(self):
        return self.opt


