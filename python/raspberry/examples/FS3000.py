# -*- coding: utf-8 -*-
"""
@file FS3000.py
@brief 这是空气流速传感器的示例代码.
@copyright  Copyright (c) 2024 DFRobot Co.Ltd (http://www.dfrobot.com)
@license     The MIT License (MIT)
@author [tangjie](jie.tang@dfrobot.com)
@version  V1.0
@date  2024-12-03
@url https://github.com/DFRobot/DFRobot_FS3000
"""

from __future__ import print_function
import sys
import os
sys.path.append("../")
import time

from DFRobot_FS3000 import *

fs = DFRobot_FS3000

def setup():
  #初始化FS3000_1005
  fs.set_range(AIRFLOW_RANGE_7_MPS)
  #屏蔽上面代码，释放下面代码，初始化FS3000_1015
  #fs.set_range(AIRFLOW_RANGE_15_MPS)
  


def loop():
    print("FS3000 Readings \tRaw: ",fs.read_raw())
    print("\tm/s: ", fs.read_meter_per_sec())
    print("\tmph: ", fs.read_mile_per_hour())
    time.sleep(1)


if __name__ == "__main__":
  setup()
  while True:
    loop()