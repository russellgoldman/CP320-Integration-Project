#!/usr/bin/python

import spidev
import time

class sensor(self):
    def __init__:
        adc_channel=1

        spi=spidev.SpiDev()
        spi.open(0,1)
        spi.max_speed_hz = 5000

        data_scale_count = 0
        data_scale_min = 2
        data_scale_confirm = 3

    def check_reading(self):
        try:
            while True:
                adc=spi.xfer2([1,(8+adc_channel)<<4,0])
                data=((adc[1]&3)<<8) +adc[2]
                data_scale=(data*3.3)/float(1023)
                data_scale=round(data_scale,2)

                if data_scale >= data_scale_min:
                    data_scale_count += 1
                if data_scale_count >= data_scale_confirm:
                    return True

                print (data_scale)
                time.sleep(2)
        except KeyboardInterrupt:
            pass
        spi.close()