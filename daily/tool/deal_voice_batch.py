import wave
from pydub import AudioSegment
import os
import numpy as np
import struct
from concurrent.futures import ThreadPoolExecutor


def open_file(path):
    file = open(path, 'rb')
    file_tuple = os.path.splitext(os.path.basename(file.name))
    file.close()
    song = AudioSegment.from_mp3(path)
    song.export("E:/music/temp/%s%s" % (file_tuple[0], '.wav'), format="wav")
    wf = wave.open("E:/music/temp/%s%s" % (file_tuple[0], '.wav'), 'rb')
    frames = wf.getnframes()
    framerate = wf.getframerate()
    str_data = wf.readframes(frames)
    sample_width = wf.getsampwidth()
    wf.close()
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data.shape = (-1, 2)
    wave_data = wave_data.T
    mono_wave = (wave_data[0]+wave_data[1])/2
    wf_mono = wave.open("E:/music/temp/%s%s" % (file_tuple[0], '.wav'), 'wb')
    wf_mono.setnchannels(1)
    wf_mono.setframerate(framerate)
    wf_mono.setsampwidth(sample_width)
    for i in mono_wave:
        data = struct.pack('<h', int(i))
        wf_mono.writeframesraw(data)
    wf_mono.close()
    new_song = AudioSegment.from_wav("E:/music/temp/%s%s" % (file_tuple[0], '.wav'))
    new_song = new_song + 20
    new_song.export("E:/music/dst/%s%s" % (file_tuple[0], '.mp3'), format="mp3")


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as executor:
        for root, dirs, files in os.walk("E:\music\src"):
            for name in files:
                executor.submit(open_file, os.path.join(root, name))


