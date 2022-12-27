import wave
import struct
# from pylab import *

class HighPitchHarmonicExtractor:
    def fir(x, b):
        """FIRフィルタ
        x: 入力信号
        b: フィルタ係数"""
        y = [0.0] * len(x)  # フィルタの出力信号
        N = len(b)      # フィルタ係数の数
        for n in range(len(x)):
            for i in range(N):
                if n - i >= 0:
                    y[n] += b[i] * x[n - i]
        return y

    def save(data, fs, bit, filename):
        """波形データをWAVEファイルへ出力"""
        wf2 = wave.open(filename, "w")
        wf2.setnchannels(2)
        wf2.setsampwidth(bit // 8)
        wf2.setframerate(fs)
        wf2.writeframes(data)

        print('書き込みファイル---------------------------------------------------')
        print('チャンネル数:', wf2.getnchannels())  # モノラルなら1，ステレオなら2
        print('サンプル幅:', wf2.getsampwidth())  # バイト数 (1byte=8bit)
        print('サンプリング周波数:', wf2.getframerate())  # CDは44100Hz
        print('フレーム数:', wf2.getnframes())  # サンプリング周波数で割れば時間
        # print('パラメータ:', wf.getparams())  # 上記+αのパラメータをタプルで返す
        print('----------------------------------------------------------------')

        wf2.close()

    def generate(self, src_file_dir, src_file_name):
        wf = wave.open(src_file_dir + '\\' + src_file_name, "r")

        print('読み込みファイル---------------------------------------------------')
        print('チャンネル数:', wf.getnchannels())  # モノラルなら1，ステレオなら2
        print('サンプル幅:', wf.getsampwidth())  # バイト数 (1byte=8bit)
        print('サンプリング周波数:', wf.getframerate())  # CDは44100Hz
        print('フレーム数:', wf.getnframes())  # サンプリング周波数で割れば時間
        print('パラメータ:', wf.getparams())  # 上記+αのパラメータをタプルで返す
        print('----------------------------------------------------------------')

        fs = wf.getframerate()

        x = wf.readframes(wf.getnframes())
        x = frombuffer(x, dtype="int16") / 32768.0  # -1 ~ 1

        # FIRフィルタをかける
        b = [1, -0.97]
        y = fir(x, b)

        # 正規化前のバイナリデータに戻す
        y = [int(v * 32767.0) for v in y]

        for i in range(len(y)):
            # if y[i] < -32768 or 32767 < y[i]:
            #     print(y[i])
            # else:
            #     continue
            if y[i] < -32768:
                y[i] = -32768
            elif 32767 < y[i]:
                y[i] = 32767

        y = struct.pack("h" * len(y), *y)

        # 音声を保存
        save(y, fs, 16, src_file_dir + '\\percussive_file_5.wav')


