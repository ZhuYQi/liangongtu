"""
Author: ZhuYQi<17120760@bjtu.edu.cn>
Date: 2020-1-26
"""

import random
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter


def scanLianGong():
    txt = open('练功.txt', encoding='utf-8').readlines()[0]
    for char_ in txt:
        print(ord(char_))


# 经分析字符的ord(char_)
# 查到了神功出自埃及象形文字
# 介绍链接：
# http://www.alanwood.net/unicode/egyptian-hieroglyphs.html
# 可惜的是，这类字符只被少数字体支持
# 比如本例提供的Segoe ui historic.ttf


def saveAllEgyptianHieroglyphs():
    msyh = ImageFont.truetype(font='Segoe ui historic.ttf', size=175)

    def drawChar(char, file_name):
        im = Image.new("RGB", (200, 200), 'white')
        d = ImageDraw.Draw(im)
        location = (35, -25)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        d.text(location, char, font=msyh, fill=color)
        im.save(file_name)

    import os
    if not os.path.exists('images'):
        os.mkdir('images')

    for i in range(77824, 78895):
        char_ = chr(i)
        file_path_ = "images/%d.png" % i
        drawChar(char_, file_path_)


def animationCreation():
    fig = plt.figure()

    ims = []
    for i in range(77824, 78895):
        # print(i)
        file_path_ = "images/%d.png" % i
        im = plt.imshow(plt.imread(file_path_), animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=20, blit=True, repeat=False)

    writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    ani.save("movie.mp4", writer=writer)


if __name__ == '__main__':
    scanLianGong()
    saveAllEgyptianHieroglyphs()
    animationCreation()
