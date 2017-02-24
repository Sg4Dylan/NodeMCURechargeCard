## NodeMCURechargeCard  
使用基于 ESP8266 的 NodeMCU 及 RC522 对 Mifare Class 1K 卡片充值  
Using NodeMCU (base on ESP8266) and RC522 to recharge your Mifare Class 1K card

####依赖 dependence  

 - [NodeMCU](https://github.com/nodemcu/nodemcu-devkit-v1.0)
 - [MicroPython](https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html)
 - [micropython-mfrc522](https://github.com/wendlers/micropython-mfrc522)

#### 使用方法 Usage  

 1. 上载脚本 Upload scripts  

> ampy --port COM5 put mfrc522.py mfrc522.py
> ampy --port COM5 put charge_card.py charge_card.py

 2. 运行脚本 Run script  

> import charge_card.py

#### 其他 Others  
注意：脚本运行后将读取并修改 charge_card.py 中第六行所标记的区块的前两个字节共 16 位。读写使用的该扇区 KeyA 位于 charge_card.py 中第七行。  
Note: After the script is run, it will read and modify the first two bytes of the block marked by the sixth line in charge_card.py. The sector used to read and write KeyA is located in the seventh line of charge_card.py.



