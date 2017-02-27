#from mipow_comet import *
import mipow_comet

bulb = mipow_comet.mipow_comet("70:44:4B:14:AC:E6")
bulb.connect()
#bulb.on()
#bulb.set_wrgb(0x00, 0x47, 0x00, 0x88)
bulb.set_rgb(0x47, 0x00, 0x88)
#bulb.set_wrgb(0xff, 0x00, 0x00, 0x00)

#bulb.set_brightness(255)

#bulb.set_effect(0x47, 0x00, 0x88, 0xff, 0x14)

print(bulb.get_brightness())

bulb.disconnect()
