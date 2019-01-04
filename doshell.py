import os
import sys
import glob
import time
import subprocess

PATH = "/home/ubuntu/下载/TF卡/"
sys.path.append(PATH)

videopath = glob.glob(PATH+"*.mp4")
times = time.time()

for indx,video in enumerate(videopath):
    name = os.path.splitext(os.path.split(video)[1])[0]
    end = time.time() - times
    try:
        subprocess.call("ffmpeg -i {} -r 1.5 -f image2 {}%d.jpg".format(video,PATH+str(end)),shell=True)
        print("截取视频:{}".format(video))
    except:
        print("{}截取失败".format(video))
        continue