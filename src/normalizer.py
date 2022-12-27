import ffmpeg_normalize

ffmpegNormalize = ffmpeg_normalize.FFmpegNormalize()

def ffmpeg_normalize_call(music_file_path):
    print(' ****************************************')
    print(' Start : Normalize ' + music_file_path)
    print(' ****************************************')

    normalized_file_path = ''
    # if music_file_path.endswith('.mp3'):
    #     normalized_file_path = music_file_path.replace('.mp3', '_normalize.mp3')
    # elif music_file_path.endswith('.wav'):
    #     normalized_file_path = music_file_path.replace('.wav', '_normalize.wav')
    # ffmpegNormalize.add_media_file(music_file_path, normalized_file_path)

    ffmpegNormalize.add_media_file(music_file_path, music_file_path)
    ffmpegNormalize.run_normalization()

    print(' ****************************************')
    print('  End  : Normalize ' + music_file_path)
    print(' ****************************************')

class Normalizer:

    # 初期処理
    def __init__(self):
        print("Normalizer.__init__")

    # # args: music file
    # def ffmpeg_normalize_call(self, music_file_path):
    #     print(' ****************************************')
    #     print(' Start : Normalize ' + music_file_path)
    #     print(' ****************************************')
    #
    #     normalized_file_path = ''
    #     # if music_file_path.endswith('.mp3'):
    #     #     normalized_file_path = music_file_path.replace('.mp3', '_normalize.mp3')
    #     # elif music_file_path.endswith('.wav'):
    #     #     normalized_file_path = music_file_path.replace('.wav', '_normalize.wav')
    #     # ffmpegNormalize.add_media_file(music_file_path, normalized_file_path)
    #
    #     ffmpegNormalize.add_media_file(music_file_path, music_file_path)
    #     ffmpegNormalize.run_normalization()
    #
    #     print(' ****************************************')
    #     print('  End  : Normalize ' + music_file_path)
    #     print(' ****************************************')
