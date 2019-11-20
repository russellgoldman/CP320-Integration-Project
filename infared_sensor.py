#!/usr/bin/python

import spidev
import time

class sensor():
    def __init__(self):
        self.adc_channel=1

        self.spi=spidev.SpiDev()
        self.spi.open(0,1)
        self.spi.max_speed_hz = 5000

        self.data_scale_count = 0
        self.data_scale_min = 1.5
        self.data_scale_confirm = 3

    def check_reading(self):
        try:
            i = 0
            while i < 10:
                adc=self.spi.xfer2([1,(8+self.adc_channel)<<4,0])
                data=((adc[1]&3)<<8) + adc[2]
                data_scale=(data*3.3)/float(1023)
                data_scale=round(data_scale,2)
                print(data_scale)

                if data_scale >= self.data_scale_min:
                    self.data_scale_count += 1
                if self.data_scale_count >= self.data_scale_confirm:
                    return True

                time.sleep(2)
                i += 1
        except KeyboardInterrupt:
            pass
        self.spi.close()