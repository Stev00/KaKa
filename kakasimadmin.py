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
    time.sleep(2)
    #time.sleep(random.randint(3,5))

def Press_Number(x):
    if int(x) == 0:
        CMD('adb -s N0AE270111 shell input tap 266 1476')
    elif int(x) == 1:
        CMD('adb -s N0AE270111 shell input tap 93 1171')
    elif int(x) == 2:
        CMD('adb -s N0AE270111 shell input tap 258 1180')
    elif int(x) == 3:
        CMD('adb -s N0AE270111 shell input tap 429 1174')
    elif int(x) == 4:
        CMD('adb -s N0AE270111 shell input tap 84 1271')
    elif int(x) == 5:
        CMD('adb -s N0AE270111 shell input tap 266 1261')
    elif int(x) == 6:
        CMD('adb -s N0AE270111 shell input tap 439 1281')
    elif int(x) == 7:
        CMD('adb -s N0AE270111 shell input tap 101 1378')
    elif int(x) == 8:
        CMD('adb -s N0AE270111 shell input tap 287 1382')
    elif int(x) == 9:
        CMD('adb -s N0AE270111 shell input tap 438 1375')
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Wrong press number')

def Operator_Login():
    CMD('adb -s N0AE270111 shell input keyevent 224') #liang
    CMD('adb -s N0AE270111 shell input swipe 344 1593 324 581')
    CMD('adb -s N0AE270111 shell am force-stop com.tencent.wework')
    CMD('adb -s N0AE270111 shell am start -n com.tencent.wework/.launch.LaunchSplashActivity')
    CMD('adb -s N0AE270111 shell input tap 541 883') #queding
    CMD('adb -s N0AE270111 shell input tap 37 120') #tui
    CMD('adb -s N0AE270111 shell input tap 359 1423') #shoujihao
    CMD('adb -s N0AE270111 shell input tap 402 329') #diankuang
    for p in list(str(15332361778)):
        Press_Number(p)
    CMD('adb -s N0AE270111 shell input tap 345 446') #next
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'send yanzhengma')
    time.sleep(120)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'pulling...')
    CMD('git pull')
    with open('YZ.txt', 'rt') as file:
        YZM = eval(file.read())
    for q in list(str(YZM)):
        Press_Number(q)
    CMD('adb -s N0AE270111 shell input tap 447 510') #next
    CMD('adb -s N0AE270111 shell input tap 345 608 ') #jinru
    time.sleep(3)
    CMD('adb -s N0AE270111 exec-out screencap -p > E:\pull\sc_l.png')
    CMD('adb -s N0AE270111 shell input keyevent 223') #mie

def Operate_Phone():
    CMD('adb -s N0AE270111 shell input keyevent 224') #liang
    #CMD('adb -s N0AE270111 shell getevent -l')
    CMD('adb -s N0AE270111 shell input swipe 344 1593 324 581')
    CMD('adb -s N0AE270111 shell svc bluetooth enable')
    #CMD('look_app_package.py')
    CMD('adb -s N0AE270111 shell am force-stop com.tencent.wework')
    CMD('adb -s N0AE270111 shell am start -n com.tencent.wework/.launch.LaunchSplashActivity')
    time.sleep(5)
    CMD('adb -s N0AE270111 shell input tap 468 1505')
    CMD('adb -s N0AE270111 shell input tap 356 303') #aidaka(3:586 299) 13:24A_12B 12:166_157 HEX->DEC
    time.sleep(10)
    CMD('adb -s N0AE270111 exec-out screencap -p > E:\pull\sc_d.png')
    CMD('adb -s N0AE270111 shell svc bluetooth disable')
    CMD('adb -s N0AE270111 shell input keyevent 223') #mie
    #CMD('adb -s N0AE270111 shell input keyevent 26') #power key

def Git_push():
    CMD('git add .')
    CMD('git commit -m "local number"')
    CMD('git push origin master')

def use_phone_net():
    CMD('adb root')
    CMD('adb shell settings put global airplane_mode_on 0')
    CMD('adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false')
    CMD('netsh interface set interface "WAN_LOCAL" disabled')
    time.sleep(3)
    CMD('netsh interface set interface "NET_USB" enabled')
    time.sleep(3)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'neting')

def unuse_phone_net():
    CMD('adb root')
    CMD('adb shell settings put global airplane_mode_on 1')
    CMD('adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true')
    #CMD('netsh interface set interface "WAN_LOCAL" enabled')
    time.sleep(3)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'unnet')


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'initing..')
    start_time_am = '08:01:00'
    end_time_am =  '08:59:59'
    #end_time_am =  '17:49:59'
    start_time_pm = '18:25:00'
    end_time_pm =  '19:40:59'
    n=1
    l=1
    with open('Result_daka.txt', 'wt',encoding="utf-8") as file:
        file.write(str(time.strftime("%H:%M:%S", time.localtime())))
    with open('Result_login.txt', 'wt',encoding="utf-8") as file:
        file.write(str(time.strftime("%H:%M:%S", time.localtime())))
    with open('dakaYN.txt', 'wt',encoding="utf-8") as file:
        file.write('999')
    with open('loginYN.txt', 'wt',encoding="utf-8") as file:
        file.write('999')
    with open('YZ.txt', 'wt',encoding="utf-8") as file:
        file.write('999999')
    use_phone_net()
    Git_push()
    unuse_phone_net()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Root 111 Phone')
    CMD('adb -s N0AE270111 root')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'wait 30s')
    time.sleep(30)


    while True:
        now_localtime = time.strftime("%H:%M:%S", time.localtime())
        if start_time_am < now_localtime < end_time_am or start_time_pm < now_localtime < end_time_pm:
            use_phone_net()
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'pulling...')
            CMD('git pull')
            with open('dakaYN.txt', 'rt') as file:
                Yes_Number = eval(file.read())
            with open('loginYN.txt', 'rt') as file:
                Yes_Login = eval(file.read())

            if l == Yes_Login:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Nice Number,Starting login...')
                Operator_Login()
                l += 1
                content_login = pytesseract.image_to_string(Image.open(r'..\sc_l.png'), lang='chi_sim')
                with open('Result_login.txt', 'wt',encoding="utf-8") as file:
                    file.write('Login Waiting'+str(l)+'_'+content_login)
                Git_push()
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Finish login...')
                time.sleep(2)
            else:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Wrong login Number')
                
            if n == Yes_Number:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Nice Number,Starting DK...')
                Operate_Phone()
                n += 1
                content_daka = pytesseract.image_to_string(Image.open(r'..\sc_d.png'), lang='chi_sim')
                with open('Result_daka.txt', 'at',encoding="utf-8") as file:
                    file.write('Number Waiting'+str(n)+'_'+content_daka)
                Git_push()
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Finish DK...')
                time.sleep(2)
            else:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Wrong DK Number,waiting...')
            unuse_phone_net()
            time.sleep(random.randint(468,498))
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'out time waiting...')
            time.sleep(random.randint(450,700))
            continue