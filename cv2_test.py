import cv2
import numpy as np
import config
import util
import sink


im = np.ones(shape=(config.frame_height, config.frame_width,3), dtype=np.int16)

with sink.ffmpeg() as f:
    while True:
        cv2.rectangle(im, pt1=util.random_xy(), pt2=util.random_xy(), color=(255, 255, 0), thickness=1)
        f.write(im.tobytes())
