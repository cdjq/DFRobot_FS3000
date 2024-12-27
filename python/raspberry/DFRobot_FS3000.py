# -*- coding: utf-8 -*
'''!
    @file        DFRobot_FS3000.py
    @brief       这是空气流速模块驱动库.
    @copyright   Copyright (c) 2024 DFRobot Co.Ltd (http://www.dfrobot.com)
    @license     The MIT License (MIT)
    @author      TangJie(jie.tang@dfrobot.com)
    @version     V1.0
    @date        2024-12-02
    @url         https://github.com/DFRobot/DFRobot_FS3000
'''
import time
import smbus

AIRFLOW_RANGE_7_MPS = 9
AIRFLOW_RANGE_15_MPS = 13

class DFRobot_FS3000:

    def __init__(self):
        self._addr = 0x28
        self.i2c = smbus.SMBus(1)
        self._range = 0
        self._mpsDataPoint = [0] *14
        self._rawDataPoint = [0] *14
        self.mpsDataPoint_7_mps = [0, 1.07, 2.01, 3.00, 3.97, 4.96, 5.98, 6.99, 7.23]
        self.rawDataPoint_7_mps = [409, 915, 1522, 2066, 2523, 2908, 3256, 3572, 3686]
        self.mpsDataPoint_15_mps = [0, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 13.00, 15.00]
        self.rawDataPoint_15_mps =  [409, 1203, 1597, 1908, 2187, 2400, 2629, 2801, 3006, 3178, 3309, 3563, 3686]


    def set_range(self, range):
        '''
        @fn set_range
        @brief 设置空气流速检测距离
        @range AIRFLOW_RANGE_7_MPS:FS3000_1005 AIRFLOW_RANGE_15MPS:FS3000_1015
        '''
        self._range = range
        
        if self._range == AIRFLOW_RANGE_7_MPS:
            self._mpsDataPoint = list(self.mpsDataPoint_7_mps)#self.mpsDataPoint_7_mps.copy()
            self._rawDataPoint = list(self.rawDataPoint_7_mps)#self.rawDataPoint_7_mps.copy()
        elif self._range == AIRFLOW_RANGE_15_MPS:
            self._mpsDataPoint = self.mpsDataPoint_15_mps.copy()
            self._rawDataPoint = self.rawDataPoint_15_mps.copy()

    def read_raw(self):
        '''
        @fn read_raw
        @brief 获取传感器得原始数据
        @return FS3000 寄存器原始数据
        '''
        self.ret = 0
        readBuf = self._read_data()
        if self._check_sum(readBuf):
            self.ret = readBuf[1] << 8 | readBuf[2]
        return self.ret
    
    def read_meter_per_sec(self):
        '''
        @fn read_meter_per_sec
        @brief 获取米/秒为单位的空气流速
        @return 空气流速数据
        '''
        self.data_position = 0
        self.air_flow_raw = self.read_raw()

        if (self.air_flow_raw < 409):
            return 0
        elif (self.air_flow_raw >= 3686):
            if self._range == AIRFLOW_RANGE_7_MPS:
                return 7.23
            elif self._range == AIRFLOW_RANGE_15_MPS:
                return 15.00
        
        for i in range(self._range):
            if (self.air_flow_raw > self._rawDataPoint[i]):
                self.data_position = i

        self.window_size = self._rawDataPoint[self.data_position+1] - self._rawDataPoint[self.data_position]
        self.diff = self.air_flow_raw  - self._rawDataPoint[self.data_position]
        self.percentage_of_window = (float)self.diff / (float)self.window_size
        self.window_size_mps = self._mpsDataPoint[self.data_position+1] - self._mpsDataPoint[self.data_position]

        self.air_flow_mps = self._mpsDataPoint[self.data_position] + (self.window_size_mps * self.percentage_of_window)

        return self.air_flow_mps
    
    def read_mile_per_hour(self):
        '''
        @fn read_meter_per_sec
        @brief 获取英里/小时为单位的空气流速
        @return 空气流速数据
        '''
        return self.read_meter_per_sec() * 2.2369362912


    def _check_sum(self,buf):
        self.sum = 0
        for i in range(1, 5):
            sum += buf[i]
        self.sum &= 0xff
        if (self.sum & buf[0]) == 0:
            return True
        return False



    def _read_data(self):
        rslt = [0]*5
        for i in range(5):
            try:
                rslt[i] = self._bus.read_byte(self._addr)
            except:
                rslt[i] = 0
        return rslt