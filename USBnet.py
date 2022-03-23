import os,time

def CMD(command):
    os.system(command)
    time.sleep(2)

CMD('adb -s N0AE270111 shell input keyevent 223') #mie
CMD('adb -s N0AE270111 shell input keyevent 224') #liang
CMD('adb -s N0AE270111 shell input swipe 344 1593 324 581') #jiesuo
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'already jiesuo')
#CMD('adb -s N0AE270111 shell input swipe 344 1593 324 581') #zhujiemian
#CMD('adb -s N0AE270111 shell input tap 102 671') #66 29f HEX->DEC
CMD('adb shell am force-stop com.android.settings')
CMD('adb shell am start com.android.settings/com.android.settings.Settings')
CMD('adb -s N0AE270111 shell input tap 352 351') #160 15f HEX->DEC
CMD('adb -s N0AE270111 shell input tap 270 564') #10e 234 HEX->DEC
CMD('adb -s N0AE270111 shell input tap 651 381') #28b 17d HEX->DEC
CMD('adb shell am force-stop com.android.settings')
CMD('adb -s N0AE270111 shell input keyevent 223') #mie
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'LCM mie')