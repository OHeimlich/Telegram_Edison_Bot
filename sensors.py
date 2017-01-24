import pyupm_grove as grove
import pyupm_i2clcd as edi_lcd
from multiprocessing import Process

temperature = grove.GroveTemp(0)
led = grove.GroveLed(3)
lcd = edi_lcd.Jhd1313m1(0, 0x3E, 0x62)


def led_on():
    led.on()


def led_off():
    led.off()


def get_temp():
    return temperature.value()


def write_lcd_first_line(msg):
    # if len(msg) > 15:
    #     p = Process(target=scroll)
    #     p.start()
    lcd.setCursor(0, 0)
    lcd.write(msg)


def write_lcd_seconed_line(msg):
    # if len(msg) > 15:
    #     p = Process(target=scroll)
    #     p.start()
    lcd.setCursor(1, 0)
    lcd.write(msg)


def scroll():
    while True:
        lcd.scroll(True)


def clear_lcd():
    lcd.clear()