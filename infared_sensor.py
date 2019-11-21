#!/usr/bin/python

import spidev
import time

class sensor():
    def __init__(self):
        self.adc_channel = 1

        self.spi = spidev.SpiDev()
        self.spi.open(0,1)
        self.spi.max_speed_hz = 5000

        self.data_scale_count = 0
        self.data_scale_min = 1.5
        self.data_scale_confirm = 3

        self.LOOP_COUNT = 10
        self.START_BYTE = 1
        self.CHANNEL_INCREMENT = 8
        self.BITWISE_SHIFT = 4
        self.BITWISE_SHIFT_DEFAULT = 0

        self.ADC_START_INDEX = 1
        self.ADC_END_INDEX = 2
        self.BITWISE_AND_CHECK = 3
        self.DATA_BITWISE_SHIFT = 8

        self.DATA_SCALE_MULTIPLIER = 3.3
        self.DATA_SCALE_DIVIDER = 1023

        self.TIME_SLEEP = 2
        self.INCREMENT = 1

    def check_reading(self):
        try:
            i = 0
            while i < self.LOOP_COUNT:
                adc = self.spi.xfer2([self.START_BYTE, (self.adc_channel + self.CHANNEL_INCREMENT) << self.BITWISE_SHIFT, self.BITWISE_SHIFT_DEFAULT])
                data = ((adc[self.ADC_END_INDEX] & self.BITWISE_AND_CHECK) << self.DATA_BITWISE_SHIFT) + adc[self.ADC_END_INDEX]
                data_scale = (data * self.DATA_SCALE_MULTIPLIER) / float(self.DATA_SCALE_DIVIDER)
                data_scale = round(data_scale, self.ADC_END_INDEX)
                print(data_scale)

                if data_scale >= self.data_scale_min:
                    self.data_scale_count += self.INCREMENT
                if self.data_scale_count >= self.data_scale_confirm:
                    return True

                time.sleep(self.TIME_SLEEP)
                i += self.INCREMENT
        except KeyboardInterrupt:
            pass
        self.spi.close()