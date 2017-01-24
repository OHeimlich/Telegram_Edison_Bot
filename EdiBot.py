#!/usr/bin/python

import telepot
import time
from pprint import pprint
from sensors import *
from pyupm_grove import GroveTemp
import re
from token_ import token

def do(name, cmd):
    re_temp = r'.*temperature.*'
    re_led_on = r'.*led.*on'
    re_led_off = r'.*led.*off'
    cmd = cmd.lower()
    m_temp = re.match(re_temp, cmd)
    m_led_on = re.match(re_led_on, cmd)
    m_led_off = re.match(re_led_off, cmd)
    if m_led_on:
        led_on()
        return 'Led Turned On'
    if m_led_off:
        led_off()
        return 'Led Turned Off'
    if m_temp:
        return 'The Temperature is: {}'.format(get_temp())

    help = '''
    Hi {name}!
You can ask about the temperature or to turn the led on/off.'''.format(name=name)
    return help


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg.get('text').__str__()
    first_name = msg.get('from').get('first_name').__str__()
    act = do(first_name, text)
    bot.sendMessage(chat_id, '{}'.format(act))
    clear_lcd()
    write_lcd_first_line('{name}: {msg}'.format(name=first_name, msg=text))
    write_lcd_seconed_line('{name}: {msg}'.format(name='Bot', msg=act))
    print(content_type, chat_type, chat_id)
    pprint('Message: {}'.format(msg))


bot = telepot.Bot(token)
print bot.getMe()

bot.message_loop(handle)

while 1:
    time.sleep(10)
