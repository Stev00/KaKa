import os,time

def CMD(command):
    os.system(command)
    time.sleep(2)

def Git_push():
    CMD('git add .')
    CMD('git commit -m "local number"')
    CMD('git push origin master')


def use_phone_net():
    CMD('adb -s N0AE270111 shell input keyevent 224') #liang
    CMD('adb root')
    CMD('adb shell settings put global airplane_mode_on 0')
    time.sleep(5)
    CMD('adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false')
    #CMD('netsh interface set interface "WAN_LOCAL" disabled')
    #CMD('netsh interface set interface "NET_USB" enabled')
    time.sleep(5)
    CMD('adb -s N0AE270111 shell input keyevent 223') #mie
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'neting')

def unuse_phone_net():
    CMD('adb -s N0AE270111 shell input keyevent 224') #liang
    CMD('adb root')
    CMD('adb shell settings put global airplane_mode_on 1')
    time.sleep(5)
    CMD('adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true')
    #CMD('netsh interface set interface "WAN_LOCAL" enabled')
    #CMD('netsh interface set interface "NET_USB" disabled')
    time.sleep(8)
    CMD('adb -s N0AE270111 shell input keyevent 223') #mie
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'unnet')

if __name__ == '__main__':
    while True:
        #print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        n = input('swith0/1/9:')
        if n == str(0):
            unuse_phone_net()
        elif n == str(1):
            use_phone_net()
        elif n == str(9):
            #use_phone_net()
            Git_push()
            #unuse_phone_net()
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Wrong N.')