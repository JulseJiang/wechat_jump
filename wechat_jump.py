import os

import PIL
import numpy
from PIL import Image



def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')#获取手机当前截图
    os.system('adb pull /sdcard/screen.png')#下载当前截图到电脑当前工作文件夹下
    return numpy.array(PIL.Image.open('screen.png'))

if __name__ == '__main__':
    print('开始')
    get_screen_image()
    figure = plt

