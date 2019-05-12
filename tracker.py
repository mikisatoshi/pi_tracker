# -*- coding: utf-8 -*-
import json,datetime,time,sys
import numpy as np
import pandas as pd
import cv2
import matplotlib as plt
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
    plt.imshow(self.template)
    plt.show()




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
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) != -1:
            break
 
    cap.release()
    cv2.destroyAllWindows()


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

