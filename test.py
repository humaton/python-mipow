#from mipow_comet import *
import mipow_comet

bulb = mipow_comet.mipow_comet("70:44:4B:14:AC:E6")
bulb.connect()
bulb.on()
#bulb.set_wrgb(0x00, 0x47, 0x00, 0x88)
#bulb.set_wrgb(0xff, 0x00, 0x00, 0x00)

bulb.set_brightness(50)
bulb.disconnect()
