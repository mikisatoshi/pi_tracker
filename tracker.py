# -*- coding: utf-8 -*-
import json,datetime,time,sys
import numpy as np
import pandas as pd
import cv2
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

    pass

  def tracker(self):

    print("tracker")
    cap = cv2.VideoCapture(0)
     
    while(True):
        ret, frame = cap.read()
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

