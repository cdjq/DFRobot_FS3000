DFRobot_FS3000
===========================

* [中文版](./README_CN.md)

这是一个空气流速传感器的驱动库。

![产品效果图片](./resources/images/SEN0501.png)
![产品效果图片](./resources/images/SEN0500.png)
  
## Product Link (https://www.dfrobot.com)
    SKU: 无

## Table of Contents

  * [Summary](#summary)
  * [Installation](#installation)
  * [Methods](#methods)
  * [Compatibility](#compatibility)
  * [History](#history)
  * [Credits](#credits)

## Summary

这是一个空气流速传感器的驱动库。


## Installation

To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.

## Methods

```C++
    /**
     * @fn setRange
     * @brief 设置空气流速检测距离
     * @param range AIRFLOW_RANGE_7_MPS:FS3000_1005 AIRFLOW_RANGE_15MPS:FS3000_1015
     * @return 1：设置成功， 0：设置失败
     */
    uint8_t setRange(uint8_t range);

    /**
     * @fn readRaw
     * @brief 获取传感器得原始数据
     * @return FS3000 寄存器原始数据
     */
    uint16_t readRaw(void);

    /**
     * @fn readMeterPerSec
     * @brief 获取米/秒为单位的空气流速
     * @return 空气流速数据
     */
    float readMeterPerSec(void);

    /**
     * @fn readMilePerHour
     * @brief 获取英里/小时为单位的空气流速
     * @return 空气流速数据
     */
    float readMilePerHour(void);
```

## Compatibility

MCU                | SoftwareSerial | HardwareSerial |      IIC      |
------------------ | :----------: | :----------: | :----------: | 
Arduino Uno        |      √       |      X       |      √       |
Mega2560           |      √       |      √       |      √       |
Leonardo           |      √       |      √       |      √       |
ESP32              |      X       |      √       |      √       |
ESP8266            |      √       |      X       |      √       |
micro:bit          |      X       |      X       |      √       |
FireBeetle M0      |      X       |      √       |      √       |
Raspberry Pi       |      X       |      √       |      √       |

## History

- 2024-12-02 - Version 1.0.0 released.

## Credits

Written by TangJie(jie.tang@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))
