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

CMD('adb -s N0AE270111 root')	
CMD('adb -s N0AE270111 shell input keyevent 224') #liang

CMD('adb -s N0AE270111 shell input swipe 344 1593 324 581')


CMD('adb -s N0AE270111 shell am force-stop com.tencent.wework')
CMD('adb -s N0AE270111 shell am start -n com.tencent.wework/.launch.LaunchSplashActivity')
time.sleep(5)
CMD('adb -s N0AE270111 exec-out screencap -p > E:\pull\sc.png')
CMD('adb -s N0AE270111 shell input keyevent 223') #mie