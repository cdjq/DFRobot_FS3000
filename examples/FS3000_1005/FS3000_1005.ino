/*!
 * @file FS3000_1005.ino
 * @brief 这是FS3000_1005空气流速传感器的示例代码.
 * @copyright  Copyright (c) 2024 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license     The MIT License (MIT)
 * @author [tangjie](jie.tang@dfrobot.com)
 * @version  V1.0
 * @date  2024-12-2
 * @url https://github.com/DFRobot/DFRobot_FS3000
 */

#include "DFRobot_FS3000.h"

DFRobot_FS3000 fs;

void setup()
{
    Serial.begin(115200);

    while(!fs.setRange(AIRFLOW_RANGE_7_MPS)){
        Serial.println("Device init error");
        delay(100);
    }
    Serial.println("Device init success");

}


void loop()
{
    Serial.print("FS3000 Readings \tRaw: ");
    Serial.print(fs.readRaw()); 
    
    Serial.print("\tm/s: ");
    Serial.print(fs.readMeterPerSec()); 
    
    Serial.print("\tmph: ");
    Serial.println(fs.readMilePerHour()); 
    
    
    delay(1000); 

}

