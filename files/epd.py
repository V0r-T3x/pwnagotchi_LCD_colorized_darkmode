import logging

from . import ST7789
from . import config
from PIL import ImageOps
import pwnagotchi



class EPD(object):
    def __init__(self):
        self.reset_pin = config.RST_PIN
        self.dc_pin = config.DC_PIN
        self.width = 240
        self.height = 240
        self.st7789 = ST7789.ST7789(config.spi, config.RST_PIN, config.DC_PIN, config.BL_PIN)

    def init(self):
        logging.info("HELLO FROM EPD")
        self.st7789.Init()

    def clear(self):
        self.st7789.clear()

    def display(self, image):
        lcd_color = pwnagotchi.config['ui']['display']['color']
#        dark_mode = pwnagotchi.config['ui']['display']['darkmode']
        if pwnagotchi.config['ui']['display']['darkmode']:
            rgb_im = ImageOps.colorize(image.convert("L"), black =lcd_color, white = "black")
        else:
            rgb_im = ImageOps.colorize(image.convert("L"), black ="black", white = lcd_color)
#        logging.info(lcd_color)
        
        self.st7789.ShowImage(rgb_im, 0, 0)
