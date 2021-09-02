# 加载数据集 和 标签[并返回标签集的处理结果]
import os

import numpy as np

from daily.tool.wav2fmcc import get_wav_mfcc


def create_datasets(path):
    wavs=[]
    labels=[] # labels 和 testlabels 这里面存的值都是对应标签的下标，下标对应的名字在 labsInd 和 testlabsInd 中
    testwavs=[]
    testlabels=[]
    labsInd=[]      ## 训练集标签的名字   0：seven   1：stop
    testlabsInd=[]  ## 测试集标签的名字   0：seven   1：stop
    # 现在为了测试方便和快速直接写死，后面需要改成自动扫描文件夹和标签的形式
    #加载seven训练集

    files = os.listdir(path)
    for i in files:
        # print(i)
        waveData = get_wav_mfcc(path+i)
        # print(waveData)
        wavs.append(waveData)
        if ("seven" in labsInd)==False:
            labsInd.append("seven")
        labels.append(labsInd.index("seven"))
    #加载stop训练集
    path="D:\\wav\\stop\\"
    files = os.listdir(path)
    for i in files:
        # print(i)
        waveData = get_wav_mfcc(path+i)
        wavs.append(waveData)
        if ("stop" in labsInd)==False:
            labsInd.append("stop")
        labels.append(labsInd.index("stop"))
    #加载seven测试集
    path="D:\\wav\\test1\\"
    files = os.listdir(path)
    for i in files:
        # print(i)
        waveData = get_wav_mfcc(path+i)
        testwavs.append(waveData)
        if ("seven" in testlabsInd)==False:
            testlabsInd.append("seven")
        testlabels.append(testlabsInd.index("seven"))
    #加载stop测试集
    path="D:\\wav\\test2\\"
    files = os.listdir(path)
    for i in files:
        # print(i)
        waveData = get_wav_mfcc(path+i)
        testwavs.append(waveData)
        if ("stop" in testlabsInd)==False:
            testlabsInd.append("stop")
        testlabels.append(testlabsInd.index("stop"))

    wavs=np.array(wavs)
    labels=np.array(labels)
    testwavs=np.array(testwavs)
    testlabels=np.array(testlabels)
    return (wavs,labels),(testwavs,testlabels),(labsInd,testlabsInd)
