import mipow_comet

bulb = mipow.mipow("70:44:4B:14:AC:E6")
bulb.connect()
bulb.on()
bulb.set_wrgb(0x00, 0x47, 0x00, 0x88)
bulb.disconnect()
