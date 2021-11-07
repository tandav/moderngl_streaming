import cv2
import numpy as np
import config
import util
import sink


im = np.ones(shape=(config.frame_height, config.frame_width,3), dtype=np.int16)
font = cv2.FONT_HERSHEY_SIMPLEX


with sink.ffmpeg() as f:
    while True:
        im[...] = 0
        cv2.rectangle(im, pt1=util.random_xy(), pt2=util.random_xy(), color=(255, 255, 0), thickness=10)
        cv2.putText(im, util.random_text(), util.random_xy(), font, fontScale=1, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        f.write(im.tobytes())
