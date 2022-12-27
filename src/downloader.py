import yt_dlp as youtube_dl
from const.download_consts import DownloadCodec


class DownloadFromYoutube:

    def main(self, url, codecs):
        print(' ****************************************')
        print(' Start : Download from Youtube')
        print(' ****************************************')
        file_name = ''

        for codec in codecs:
            ydl = youtube_dl.YoutubeDL(DownloadCodec.get_by_id(codec.id).opt)
            info_dict = ydl.extract_info(url, download=True)
            file_name = info_dict['title']

        print(' ****************************************')
        print('  End  : Download from Youtube')
        print('         => ' + file_name)
        print(' ****************************************')

        return file_name
