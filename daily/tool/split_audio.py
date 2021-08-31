from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

from daily.tool import utils
from daily.tool.split_words import SplitWords


class SplitAudio():

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.__sound_file_path__ = []
        self.dirs = {}

    def split(self):

        sound_file_path = self.__get_sounds_files__()
        print(sound_file_path)
        print(self.dirs)
        print(self.__sound_file_path__)
        for d in self.dirs:
            print(d)
            for file in sound_file_path:
                print(file)
                self.__split_voice__(file, d)
        print("ok")

    def __split_voice__(self, wav_file, sq_wds):
        sound = AudioSegment.from_mp3(wav_file)
        today = utils.get_today_str()
        ind = sq_wds.index(today)
        word = sq_wds[ind + len(today):]
        try_split_times = 10
        min_silence_len = 400 # 1 sounds speak 2 or 3 words
        speak_time = 40
        keep_silence = 500
        while True:
            # try 10 times to split ,otherwise split false
            if try_split_times == 0:
                print("分割失败", wav_file)
                return False
            try_split_times = try_split_times - 1
            # min_silence_len以沉默500毫秒，切割音频文件
            # #silence_thresh 低于45分贝的声音过滤
            # keep_silence为截出的每个音频添加多少ms无声
            chunks = split_on_silence(sound, min_silence_len=min_silence_len, silence_thresh=-45,
                                      keep_silence=keep_silence)
            print(len(word), len(chunks))
            if len(word) == len(chunks):
                print('总分段：', len(chunks),'成功')
                for i, chunk in enumerate(chunks):
                    if os.path.exists(self.out_path + "chunk{0}.wav".format(word[i])):
                        os.remove(self.out_path + "chunk{0}.wav".format(word[i]))
                    chunk.export(self.out_path + "chunk{0}.wav".format(word[i]), format="wav")
                return True
            elif len(word) > len(chunks):  # voice is splited less than exception
                min_silence_len = min_silence_len - speak_time
                keep_silence = keep_silence + speak_time
                print('尝试分段：', len(chunks), '少了')
            else:  # voice is split more than exception
                min_silence_len = min_silence_len + speak_time
                keep_silence = keep_silence - speak_time
                print('尝试分段：', len(chunks), '多了')

    def __split_dir__(self, path, sample_dir=None):
        dir = os.listdir(path)
        today = utils.get_today_str()
        for d in dir:
            full_path = os.path.abspath(os.path.join(path, d))
            if os.path.isdir(full_path):
                self.__split_dir__(path=full_path, sample_dir=d)
            else:  # path is not a dir
                if full_path.find(today) < 0:
                    continue
                self.dirs[str(sample_dir)] = sample_dir
                self.__sound_file_path__.append(full_path)

    def __get_sounds_files__(self):
        self.__split_dir__(self.path)
        return self.__sound_file_path__


if __name__ == "__main__":
    p = r"D:/data/voice"
    o = r"D:/data/out/"
    sa = SplitAudio(p, o)
    sa.split()
