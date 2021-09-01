# -*- coding: utf-8 -*-
import pyaudio  #导入库
import wave   #导入wav音频库
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog
from pya import Ui_Form
import threading

class Win(QWidget,Ui_Form):
    def __init__(self):
        super(Win, self).__init__()
        self.CHUNK = 1024  # 定义数据流块--每次读取数据的字节数
        self.FORMAT = pyaudio.paInt16  #16int
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 5  # 录音时间
        self.WAVE_OUTPUT_FILENAME = "D:/data/output.wav"   #录音时要写入的文件名
        self.p = pyaudio.PyAudio()  # 创建播放器
        self.data=''
        self.setupUi(self)
        self.over = False


    def openAudioFile(self):#打开文件
        self.r = QFileDialog.getOpenFileName(self, '请选择要打开的文件', '.\\', 'WAV(*.wav)',
                                        'WAV(*.wav)')
        self.lineEdit.setText(self.r[0])

    def beginAudio(self):#录音开始
        self.t1 = threading.Thread(target=self.beginAudio2)  # 创建线程
        self.t1.setDaemon(True)  # 守护线程
        self.t1.start()

    def beginAudio2(self):
        self.stream1 = self.p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)  # 打开数据流
        self.frames = []
        n=0
        while not(self.stream1.is_stopped()):
            if self.over:
                self.over = False
                return
            data = self.stream1.read(self.CHUNK)      #从麦克风读取数据
            self.frames.append(data)
            print(data,n)
            n=n+1

    def overAudio(self):#录音结束
        self.over =True
        self.t2 = threading.Thread(target=self.overAudio2)  # 创建线程
        self.t2.setDaemon(True)  # 守护线程
        self.t2.start()

    def overAudio2(self):
        self.over = True
        self.stream1.stop_stream()  # 停止录音流
        self.stream1.close()  #关闭录音流

        # 写入录音文件
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def gono(self):  #继续
        if self.data != '' and self.stream.is_stopped():
            self.stream.start_stream()  #继续流
                # stream.close()之后就不能继续了
            self.player()

    def pauseAudio(self):#暂停
        if self.data != '':
            self.stream.stop_stream()  # 停止数据流--暂停
        # 一旦流停止，就不能调用写或读
        # 指针位置不变


    def stopAudio(self):#停止
        self.stream.stop_stream()
        self.stream.close()  #关闭流
        self.data=''
        #说明：我找不到判断流是否打开的函数，我用self.data=''表示流已经关闭
        self.wf.close()

    def player2(self):
        if self.data=='' and self.lineEdit.text()!='':
            self.wf = wave.open(self.r[0], 'rb')
            self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                      channels=self.wf.getnchannels(), rate=self.wf.getframerate(),
                                      output=True)  # 打开数据流--【获取音频格式信息】
            # output=True   输出的意思
            self.data = self.wf.readframes(self.CHUNK)  # 读取数据
        while (self.data) != '' and not(self.stream.is_stopped() ):
            #self.stream.is_stopped()  流是否停止，如果停止返回True

            self.stream.write(self.data)  #播放
            #注意事项：播放时占用线程，最好创建一个线程
            self.data = self.wf.readframes(self.CHUNK)

    def player(self):  #播放
        self.t = threading.Thread(target=self.player2)  #创建线程
        self.t.setDaemon(True)  #守护线程
        self.t.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Win()
    demo.show()
    sys.exit(app.exec_())
