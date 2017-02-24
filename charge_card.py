import mfrc522
from os import uname

def go_work():

    target_sector = 0x26 # 0x00 - 0x3F
    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF] # Sector KeyA

    if uname()[0] == 'WiPy':
        rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
    elif uname()[0] == 'esp8266':
        rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
    else:
        raise RuntimeError("Unsupported platform")

    print("")
    print("Place card and wait.")
    print("")

    try:
        while True:

            (stat, tag_type) = rdr.request(rdr.REQIDL)

            if stat == rdr.OK:
                # DETECT COIL
                (stat, raw_uid) = rdr.anticoll()
                # DETECTED
                if stat == rdr.OK:
                    print("New card detected")
                    print("  - tag type: 0x%02x" % tag_type)
                    print("  - uid     : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")
                    # SELECT CARD
                    if rdr.select_tag(raw_uid) == rdr.OK:
                        # CORE
                        if rdr.auth(rdr.AUTHENT1A, target_sector, key, raw_uid) == rdr.OK:
                            # READ DATA
                            read_list = rdr.read(target_sector)
                            print("Raw block data: %s" % read_list)
                            rest_value = read_list[1] * 0xFF + read_list[0]
                            print("Rest value : %s" % rest_value)
                            # Receive input value
                            str_value = ""
                            int_value = 0
                            value_flag = True
                            while value_flag:
                                str_value = input("Input value whatever you want. Less than 4096 -> ")
                                try:
                                    int_value = int(str_value)
                                    if int_value > 0 and int_value < 4096:
                                        value_flag = False
                                except:
                                    pass
                            # Convert input to data
                            read_list[0] = int_value-int(int_value/0xFF)*0xFF
                            read_list[1] = int(int_value/0xFF)
                            changed_data = ''
                            for i in read_list:
                                changed_data += str(chr(i))
                            # WRITE DATA
                            stat = rdr.write(target_sector, changed_data.encode())
                            if stat == rdr.OK:
                                print("Data blk0 written to card")
                            else:
                                print("Failed to write data to blk0")
                            rdr.stop_crypto1()
                            # DONE
                            print("Work done, please remove your card.")
                        else:
                            print("Authentication error")
                    else:
                        print("Failed to select tag")

    except KeyboardInterrupt:
        print("Bye")

go_work()