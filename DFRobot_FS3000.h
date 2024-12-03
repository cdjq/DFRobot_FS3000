/**
 * @file DFRobot_FS3000.h
 * @brief 这是空气流速模块驱动库的构造函数
 * @copyright Copyright (c) 2024 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license The MIT License (MIT)
 * @author    [TangJie](jie.tang@dfrobot.com)
 * @version   V1.0
 * @date      2024-12-02
 * @url https://github.com/DFRobot/DFRobot_FS3000
 */

#ifndef _DFROBOT_FS3000_
#define _DFROBOT_FS3000_

#include "Arduino.h"
#include "Wire.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define FS3000_ADDR 0x28
#define AIRFLOW_RANGE_7_MPS 0x09
#define AIRFLOW_RANGE_15_MPS 0x0D

#define ENABLE_DBG ///< Enable this macro to view the detailed execution process of the program.
#ifdef ENABLE_DBG
#define DBG(...) {Serial.print("[");Serial.print(__FUNCTION__); Serial.print("(): "); Serial.print(__LINE__); Serial.print(" ] "); Serial.println(__VA_ARGS__);}
#else
#define DBG(...)
#endif

class DFRobot_FS3000
{
public:
    /**
     * @fn DFRobot_FS3000
     * @brief FS3000传感器得构造函数
     * @param pWire I2C同行对象
     * @return NULL
     */
    DFRobot_FS3000(TwoWire *pWire=&Wire);

    /**
     * @fn ~DFRobot_FS3000
     * @brief FS3000传感器得析构函数
     */
    ~DFRobot_FS3000(void){
        _pWire->end();
    };

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


private:
    TwoWire *_pWire;

    uint8_t readData(void* buf, uint8_t len);
    bool checkSum(void* buf);
    float _mpsDataPoint[13]; 
    int _rawDataPoint[13]; 


};

#endif
