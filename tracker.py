# -*- coding: utf-8 -*-
import json,datetime,time,sys
import numpy as np
import pandas as pd
import cv2
from matplotlib import pylab as plt
from sklearn.covariance import EmpiricalCovariance, MinCovDet
try:
  import ADS1x15
except:
  pass

try:
  import RPi.GPIO as GPIO
except:
  pass 


class PiTracker():
  def __init__(self, mode = 0, para_path = "hoge"):
    self.template = cv2.imread('template.JPG')  # テンプレート画像
    cv2.imshow('aaa',self.template)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





  def tracker(self):
    """
    to find property identifier
    the https://docs.opencv.org/3.1.0/d8/dfe/classcv_1_1VideoCapture.html

    """

    print("tracker")
    cap = cv2.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,640)
    cap.set(5,5)
     
    while(True):
        ret, frame = cap.read()
        results = cv2.matchTemplate(frame, self.template, cv2.TM_CCOEFF_NORMED)

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(results)
        print('max value: {}, position: {}'.format(maxVal, maxLoc))
        drawn = frame.copy()
        self.draw_window(drawn, maxLoc[0], maxLoc[1], 90, 100)

        cv2.imshow('frame',drawn)
        if cv2.waitKey(1) != -1:
            break
 
    cap.release()
    cv2.destroyAllWindows()

  def draw_window(self, img, x, y, w, h):
    '''
    Args:
        img: 描画対象の画像
        x: 検索窓の左上の x 座標
        y: 検索窓の左上の y 座標
        w: 検索窓の幅
        h: 検索窓の高さ
    '''
    tl = x, y  # 左上の頂点座標
    br = x + w, y + h  # 右下の頂点座標
    cv2.rectangle(img, tl, br, (0, 255, 0), 2)




def main():
  print("main")

  # value = sys.argv
  # print(value)
  # try:
  #   runmode = int(value[1])
  # except:
  #   runmode = 0

  TKR = PiTracker()

  TKR.tracker()  




if __name__ == '__main__':

  main()

