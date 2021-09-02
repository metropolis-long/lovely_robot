import keras
from keras import Sequential
from keras.layers import Dense

from daily.voiceModel.voice_data_deal import create_datasets

path = "D:\\data\\voice\\out\\"
(wavs, labels), (testwavs, testlabels), (labsInd, testlabsInd)=create_datasets(path)
# 构建一个4层的模型
model = Sequential()
model.add(Dense(512, activation='relu',input_shape=(16000,))) # 音频为16000帧的数据，这里的维度就是16000，激活函数直接用常用的relu
model.add(Dense(256, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(5, activation='softmax'))  # 因为只有两个类别的语音，最后输出应该就是2个分类的结果
# [编译模型] 配置模型，损失函数采用交叉熵，优化采用Adadelta，将识别准确率作为模型评估
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
#  validation_data为验证集
model.fit(wavs, labels, batch_size=4, epochs=5, verbose=1, validation_data=(testwavs, testlabels)) ## 进行5轮训练，每个批次124个

# 开始评估模型效果 # verbose=0为不输出日志信息
score = model.evaluate(testwavs, testlabels, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1]) # 准确度
