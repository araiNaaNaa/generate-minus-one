import ffmpeg
import inspect
from pydub import AudioSegment
from normalizer import ffmpeg_normalize_call

# normalizer = Normalizer()


class Mixer:
    output_folder = '..\\music\\'

    def __init__(self):
        print('Mixer.__init__')
        print(inspect.stack()[1].filename)
        print(inspect.stack()[1].function)

    def merge(self, temp_sound, sound):
        print('Mixer.merge')
        if temp_sound is None:
            return sound
        return temp_sound.overlay(sound, position=0)

    def main(self, dest_folder_name, vo, gt, ba, dr, pf, add_high):
        print('Mixer.main')
        output = None
        result_file_name = dest_folder_name + '_'
        if vo:
            print('Merge Vocal')
            # normalizer.ffmpeg_normalize_call(self.output_folder + dest_folder_name + '\\vocals.wav')
            sound_vo = AudioSegment.from_file(self.output_folder + dest_folder_name + '\\vocals.wav')
            output = self.merge(output, sound_vo)
            result_file_name = result_file_name + 'V'

        if gt:
            print('Merge Guitar')
            # normalizer.ffmpeg_normalize_call(self.output_folder + dest_folder_name + '\\other.wav')
            sound_gt = AudioSegment.from_file(self.output_folder + dest_folder_name + '\\other.wav')

            # + 2dB and merge
            output = self.merge(output, sound_gt + 2)
            result_file_name = result_file_name + 'G'

        if ba:
            print('Merge Bass')
            ffmpeg_normalize_call(self.output_folder + dest_folder_name + '\\bass.wav')
            sound_ba = AudioSegment.from_file(self.output_folder + dest_folder_name + '\\bass.wav')
            output = self.merge(output, sound_ba + 1)
            result_file_name = result_file_name + 'B'

        if dr:
            print('Merge drums')
            ffmpeg_normalize_call(self.output_folder + dest_folder_name + '\\drums.wav')
            sound_dr = AudioSegment.from_file(self.output_folder + dest_folder_name + '\\drums.wav')

            # + 2dB and merge
            output = self.merge(output, sound_dr + 2)
            result_file_name = result_file_name + 'D'

        if pf:
            print('Merge Piano')
            ffmpeg_normalize_call(self.output_folder + dest_folder_name + '\\piano.wav')
            sound_pf = AudioSegment.from_file(self.output_folder + dest_folder_name + '\\piano.wav')
            output = self.merge(output, sound_pf)
            result_file_name = result_file_name + 'p'

        if add_high:
            print('Add high')
            harmonic_high = AudioSegment.from_file(self.output_folder + dest_folder_name + '\\fir_test.wav')
            harmonic_high = harmonic_high + 6
            output = self.merge(output, harmonic_high)

        # save the result
        output.export(self.output_folder + dest_folder_name + '\\' + result_file_name + '.wav', format="wav")
        print('Export completed：', self.output_folder + dest_folder_name + '\\' + result_file_name + '.wav')

        # Create to MP3（WAV -> MP3）
        stream = ffmpeg.input(self.output_folder + dest_folder_name + '\\' + result_file_name + '.wav')
        stream = ffmpeg.output(stream, self.output_folder + dest_folder_name + '\\' + result_file_name + '.mp3')
        ffmpeg.run(stream)

# mixer = Mixer()
# # # self,      add_high, dest_folder_name, vo, gt, ba, dr, pf
# mixer.main('Angra - Carry On', True, True, True, False, False, False)
