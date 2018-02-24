import os

import PIL
import numpy
import time
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation#刷新画面用

need_update = True
#获取截图
def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')#获取手机当前截图
    os.system('adb pull /sdcard/screen.png')#下载当前截图到电脑当前工作文件夹下
    return numpy.array(PIL.Image.open('screen.png'))
#刷新图片
def update_screen_image(frame):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image()) #获取新图片
        need_update = False
    return axes_image,#返回一个元祖
#跳一跳
def jump_to_next(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x1-x2)**2+(y1-y2)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410{}'.formate(int(distance*1.35)))

#点击事件
def on_click(event, coor=[]):#(x,y) #(x1,y2)
    global need_update
    coor.append((event.xdata, event.ydata))#以元祖形式存储
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())#清空栈，触发跳动事件
    need_update = True


if __name__ == '__main__':
    print('开始')
    figure = plt.figure()#创建图片对象
    axes_image = plt.imshow(get_screen_image(), animated=True)#将获取的图片置于坐标轴上
    figure.canvas.mpl_connect('button_press_event', on_click)
    ani = FuncAnimation(figure, update_screen_image, interval=50, blit=True)#将update_screen_image返回的元祖中的第一个元素绑定到figure上
    plt.show()
