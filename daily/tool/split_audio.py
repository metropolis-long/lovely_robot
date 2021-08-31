from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
from daily.tool.split_words import SplitWords


class SplitAudio():

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.__sound_file_path__ = []
        self.dirs={}

    def split(self):
        sw = SplitWords(self.path)
        sq_wds = sw.get_split_every_word_dir()
        sound_file_path = self.__get_sounds_files__()
        print(self.dirs)
        print(self.__sound_file_path__)
        print("ok")

    def __split_voice__(self, sq_wds):
        sound = AudioSegment.from_mp3(self.path)
        try_split_times = 10
        min_silence_len = 100
        keep_silence = 500
        while True:
            # try 10 times to split ,otherwise split false
            if try_split_times == 0:
                return False
            --try_split_times
            # min_silence_len以沉默500毫秒，切割音频文件
            # #silence_thresh 低于45分贝的声音过滤
            # keep_silence为截出的每个音频添加多少ms无声
            chunks = split_on_silence(sound, min_silence_len=min_silence_len, silence_thresh=-45,
                                      keep_silence=keep_silence)
            if len(sq_wds.split(",")) == len(chunks):
                print('总分段：', len(chunks))
                for i, chunk in enumerate(chunks):
                    if os.path.exists(self.out_path + "chunk{0}.wav".format(i)):
                        os.remove(self.out_path + "chunk{0}.wav".format(i))
                    chunk.export(self.out_path + "chunk{0}.wav".format(i), format="wav")
                return True
            elif len(sq_wds.split(",")) > len(chunks):  # voice is splited less than exception
                keep_silence = keep_silence + 50
                min_silence_len = min_silence_len - 50
            else:  # voice is splited more than exception
                keep_silence = keep_silence - 50
                min_silence_len = min_silence_len + 50

    def __split_dir__(self,path,sample_dir=None):
        dir = os.listdir(path)
        for d in dir:
            full_path = os.path.abspath(os.path.join(path, d))
            if os.path.isdir(full_path):
                self.__split_dir__(path=full_path,sample_dir=d)
            else:  # path is not a dir
                self.dirs[str(sample_dir)]=sample_dir
                self.__sound_file_path__.append(full_path)

    def __get_sounds_files__(self):
        self.__split_dir__(self.path)
        return self.__sound_file_path__


if __name__ == "__main__":
    p = r"D:/data"
    o = r"D:/data/out"
    sa = SplitAudio(p, o)
    sa.split()
