# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from daily.faceModel.train_model import CNN
from daily.faceModel.face_data_deal import get_user_number

from djangoProject.settings.base_settings import CV_FACE_MODEL_PATH



if __name__ == '__main__':
    nb_classes = get_user_number()
    cv2.ocl.setUseOpenCL(False)
    # 加载模型
    model = CNN()
    model.load_weights('./model/face0826')  # 读取模型权重参数

    # 框住人脸的矩形边框颜色
    color = (0, 255, 0)

    # 捕获指定摄像头的实时视频流
    temp_dir = r"D:/data/kk/video/20210826-213754.mp4"
    
    cap = cv2.VideoCapture(temp_dir)

    # 人脸识别分类器本地存储路径
    cascade_path = CV_FACE_MODEL_PATH

    # 循环检测识别人脸
    while True:
        ret, frame = cap.read()  # 读取一帧视频

        if ret is True:

            # 图像灰化，降低计算复杂度
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue
        # 使用人脸识别分类器，读入分类器
        cascade = cv2.CascadeClassifier(cascade_path)

        # 利用分类器识别出哪个区域为人脸
        faceRects = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect

                # 截取脸部图像提交给模型识别这是谁
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                face_probe = model.face_predict(image)  # 获得预测值
                print(face_probe)
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness=2)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
                pilimg = Image.fromarray(frame)
                draw = ImageDraw.Draw(pilimg)  # 图片上打印 出所有人的预测值
                font = ImageFont.truetype("simkai.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
                y_max = 95
                for item in nb_classes:
                    draw.text((x + 25, y - y_max), '{}:{:.2%}'.format(item,face_probe[nb_classes.index(item)]), (255, 0, 0), font=font)
                    y_max = y_max - 25
                frame = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

        cv2.imshow("ShowTime", frame)

        # 等待10毫秒看是否有按键输入
        k = cv2.waitKey(10)
        # 如果输入q则退出循环
        if k & 0xFF == ord('q'):
            break

    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()
