from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

sound = AudioSegment.from_mp3("D:/01_1.wav")
loudness = sound.dBFS
outputPath = "D:/data/output/"
chunks = split_on_silence(sound,
                          # 以沉默500毫秒，切割音频文件
                          min_silence_len=80,
                          # 低于45分贝的声音过滤
                          silence_thresh=-45,
                          #为截出的每个音频添加多少ms无声
                          keep_silence=400
                          )
print('总分段：', len(chunks))
for i, chunk in enumerate(chunks):
    if os.path.exists(outputPath+"chunk{0}.wav".format(i)):
        os.remove(outputPath+"chunk{0}.wav".format(i))
    chunk.export(outputPath+"chunk{0}.wav".format(i), format="wav")
