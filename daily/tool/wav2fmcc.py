import numpy as np
import wave
import matplotlib.pyplot as plt


def get_wav_mfcc(wav_path):
    f = wave.open(wav_path,'rb')
    params = f.getparams()
    # print("params:",params)
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = f.readframes(nframes)#读取音频，字符串格式
    waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
    waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
    waveData = np.reshape(waveData,[nframes,nchannels]).T
    f.close()

    # print(waveData)

    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 300 #分辨率
    plt.specgram(waveData[0],Fs = framerate, scale_by_freq = True, sides = 'default')
    plt.ylabel('Frequency(Hz)')
    plt.xlabel('Time(s)')
    plt.title('wa')
    plt.show()

    # 对音频数据进行长度大小的切割，保证每一个的长度都是一样的【因为训练文件全部是1秒钟长度，16000帧的，所以这里需要把每个语音文件的长度处理成一样的】
    data = list(np.array(waveData[0]))
    # print(len(data))
    # while len(data)>16000:
    #     del data[len(waveData[0])-1]
    #     del data[0]
    # print(len(data))
    while len(data)<16000:
        data.append(0)
    # print(len(data))

    data=np.array(data)

    # 平方之后，开平方，取正数，值的范围在  0-1  之间
    data = data ** 2
    data = data ** 0.5
    print(data)
    return data


# get_wav_mfcc("D:/data/out/20210831ABCDE/B.wav")
# get_wav_mfcc("D:/data/voice/20210831ABCDE/0000001.wav")
get_wav_mfcc("D:/data/output.wav" )