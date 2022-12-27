# import librosa.display
# import soundfile as sf
#
#
# class HighPitchHarmonicExtractor:
#
#     def generate(self, src_file_dir, src_file_name):
#         print(' ****************************************')
#         print(' Start : Generate high pitch music file')
#         print(' ****************************************')
#
#         y_full, sr_full = librosa.load(src_file_dir + '\\' + src_file_name)
#
#         # marginを設定 => extract not harmonic sound, and percussive also.
#         # Separate strongly depends on margin increase
#         y_harmonic5, y_percussive5 = librosa.effects.hpss(y_full, margin=5.0)
#         sf.write(src_file_dir + '\\percussive_file_5.wav', y_percussive5, sr_full, 'PCM_24')
#
#         print(' ****************************************')
#         print('  End  : Generate high pitch music file')
#         print('         => ' + src_file_dir + '\\percussive_file_5.wav')
#         print(' ****************************************')
import os
import re

filepath1 = 'C:/Users/Arai Go/Downloads/04 鬼人風来.mp3'
print(os.path.splitext(os.path.basename(filepath1))[0])
print(os.path.splitext(filepath1)[1])
print(os.path.split(filepath1))
print("-----------------------------")
filepath = 'C:\\Users\\Arai Go\\Downloads\\04 鬼人,-:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊風来.mp3'
print(os.path.splitext(os.path.basename(filepath))[0])
print(os.path.splitext(filepath)[1])
print(os.path.split(filepath))

# shit = "AA**BB#@$CC 가나다-123"
# new_str = re.sub(r"[^0-9a-zA-Z\s]", "_", shit)
# print(new_str)

code_regex = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]')


# txt = input().rstrip()
cleaned_text = code_regex.sub('', filepath)
print(cleaned_text)