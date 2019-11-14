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
        self.data_scale_min = 2
        self.data_scale_confirm = 3

    def check_reading(self):
        try:
            while True:
                self.adc=self.spi.xfer2([1,(8+self.adc_channel)<<4,0])
                data=((self.adc[1]&3)<<8) +self.adc[2]
                self.data_scale=(data*3.3)/float(1023)
                self.data_scale=round(data_scale,2)

                if self.data_scale >= self.data_scale_min:
                    self.data_scale_count += 1
                if self.data_scale_count >= self.data_scale_confirm:
                    return True

                print (self.data_scale)
                time.sleep(2)
        except KeyboardInterrupt:
            pass
        self.spi.close()