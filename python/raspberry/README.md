DFRobot_FS3000
===========================

- [中文版](./README_CN.md)

这是一个空气流速传感器的驱动库。

![产品效果图](../../resources/images/SEN0501.png)
![产品效果图](../../resources/images/SEN0500.png)

## Product Link (https://www.dfrobot.com)

    SKU：SEN0500/SEN0501

## Table of Contents

  * [summary](#summary)
  * [installation](#installation)
  * [methods](#methods)
  * [compatibility](#compatibility)
  * [history](#history)
  * [credits](#credits)

## Summary

这是一个空气流速传感器的驱动库。

## Installation

Download this library to Raspberry Pi before use, then open the routine folder. Type python demox.py on the command line to execute a routine demox.py. For example, to execute the control_led.py routine, you need to enter:

```python
python FS3000.py
```

## Methods

```python
    def set_range(self, range):
        '''
        @fn set_range
        @brief 设置空气流速检测距离
        @range AIRFLOW_RANGE_7_MPS:FS3000_1005 AIRFLOW_RANGE_15MPS:FS3000_1015
        '''

    def read_raw(self):
        '''
        @fn read_raw
        @brief 获取传感器得原始数据
        @return FS3000 寄存器原始数据
        '''
    
    def read_meter_per_sec(self):
        '''
        @fn read_meter_per_sec
        @brief 获取米/秒为单位的空气流速
        @return 空气流速数据
        '''
    
    def read_mile_per_hour(self):
        '''
        @fn read_meter_per_sec
        @brief 获取英里/小时为单位的空气流速
        @return 空气流速数据
        '''
```

## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| Raspberry Pi2 |           |            |    √     |         |
| Raspberry Pi3 |           |            |    √     |         |
| Raspberry Pi4 |       √   |            |          |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |

## History

- 2021-08-31 - Version 1.0.0 released.

## Credits

Written by TangJie(jie.tang@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))
