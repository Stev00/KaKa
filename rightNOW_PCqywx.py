from PIL import Image
import pytesseract
import os,time,datetime,random
import pygetwindow as gw
import win32api
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

def CMD(command):
    os.system(command)
    time.sleep(random.randint(3,5))


def use_phone_net():
    CMD('adb root')
    CMD('adb shell settings put global airplane_mode_on 0')
    CMD('adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false')
    CMD('netsh interface set interface "WAN_LOCAL" disabled')
    time.sleep(3)

def unuse_phone_net():
    CMD('adb root')
    CMD('adb shell settings put global airplane_mode_on 1')
    CMD('adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true')
    CMD('netsh interface set interface "WAN_LOCAL" enabled')
    time.sleep(3)

use_phone_net()
CMD('adb -s N0AE270111 root')	
CMD('adb -s N0AE270111 shell input keyevent 224') #liang
CMD('adb -s N0AE270111 shell input swipe 344 1593 324 581')
CMD('adb -s N0AE270111 shell am force-stop com.tencent.wework')
CMD('adb -s N0AE270111 shell am start -n com.tencent.wework/.launch.LaunchSplashActivity')
time.sleep(5)
print('openPCwx')
time.sleep(5)
CMD('adb -s N0AE270111 shell input tap 363 1367')
time.sleep(2)
CMD('adb -s N0AE270111 shell input tap 363 1367')
CMD('adb -s N0AE270111 shell input keyevent 223') #mie
#CMD('adb -s N0AE270111 shell input keyevent 26') #power
unuse_phone_net()
time.sleep(2)