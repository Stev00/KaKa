
import random,os,time
import pygetwindow as gw
import win32api
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

def CMD(command):
    os.system(command)
    time.sleep(random.randint(3,5))

def Operate_Phone():
    CMD('adb -s N0AE270111 root')
    CMD('adb -s N0AE270111 shell input keyevent 224') 
    CMD('adb -s N0AE270111 shell input swipe 344 1593 324 581')
    CMD('adb -s N0AE270111 shell svc bluetooth enable')
    CMD('adb -s N0AE270111 shell am force-stop com.tencent.wework')
    CMD('adb -s N0AE270111 shell am start -n com.tencent.wework/.launch.LaunchSplashActivity')
    time.sleep(5)
    CMD('adb -s N0AE270111 shell input tap 468 1505')
    CMD('adb -s N0AE270111 shell input tap 356 303')
    time.sleep(10)
    CMD('adb -s N0AE270111 exec-out screencap -p > E:\pull\sc_d.png')
    CMD('adb -s N0AE270111 shell input keyevent 223') 
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
    #CMD('netsh interface set interface "WAN_LOCAL" enabled')
    time.sleep(3)

if __name__ == '__main__':
    use_phone_net()
    Operate_Phone()
    unuse_phone_net()