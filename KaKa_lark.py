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
    CMD('adb -s N0AE270111 shell am force-stop com.ss.android.lark')
    CMD('adb -s N0AE270111 shell am start -n com.ss.android.lark/com.ss.android.lark.main.app.MainActivity')
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
    #Open APP->adb shell "dumpsys window | grep mCurrentFocus"
    CMD('adb -s N0AE270111 shell am force-stop com.ss.android.lark')
    CMD('adb -s N0AE270111 shell am start -n com.ss.android.lark/com.ss.android.lark.main.app.MainActivity')
    time.sleep(5)
    CMD('adb -s N0AE270111 shell input tap '+str(int('11b',16))+' '+str(int('5f6',16)))#goto gongzuotai
    CMD('adb -s N0AE270111 shell input tap '+str(int('55',16))+' '+str(int('22e',16)))#goto daka
    CMD('adb -s N0AE270111 shell input tap '+str(int('15f',16))+' '+str(int('23b',16)))#am上
    CMD('adb -s N0AE270111 shell input tap '+str(int('179',16))+' '+str(int('308',16)))#pm下
#    CMD('adb -s N0AE270111 shell input tap '+str(int('x',16))+' '+str(int('y',16)))#pm下更
    time.sleep(10)
    CMD('adb -s N0AE270111 exec-out screencap -p > E:\Software\Gitee\sc_d.png')
    CMD('adb -s N0AE270111 shell svc bluetooth disable')
    CMD('adb -s N0AE270111 shell input keyevent 223') #mie
    #CMD('adb -s N0AE270111 shell input keyevent 26') #power key

def Git_push():
    CMD('git add .')
    CMD('git commit -m "local number"')
    CMD('git push origin master')

def Network_Reset():
    if len(gw.getWindowsWithTitle('gnirehtet')):
        gw.getWindowsWithTitle('gnirehtet')[0].close()
        time.sleep(2)
        win32api.ShellExecute(0, 'open', r'.\gnirehtet', '','',1)
        time.sleep(2)
        #gw.getWindowsWithTitle('gnirehtet')[0].minimize()
        #time.sleep(2)
    else:
        win32api.ShellExecute(0, 'open', r'.\gnirehtet', '','',1)
        time.sleep(2)
        #gw.getWindowsWithTitle('gnirehtet')[0].minimize()
        #time.sleep(2)

if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'initing..')
    start_time_am = '08:01:00'
    end_time_am =  '10:29:59'
    #end_time_am =  '17:49:59'
    start_time_pm = '18:01:00'
    end_time_pm =  '21:59:59'
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
    Git_push()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Root 111 Phone')
    CMD('adb -s N0AE270111 root')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'wait 60s')
    time.sleep(60)


    while True:
        now_localtime = time.strftime("%H:%M:%S", time.localtime())
        if start_time_am < now_localtime < end_time_am or start_time_pm < now_localtime < end_time_pm:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'pulling...')
            CMD('git pull')
            with open('dakaYN.txt', 'rt') as file:
                Yes_Number = eval(file.read())
            with open('loginYN.txt', 'rt') as file:
                Yes_Login = eval(file.read())

            if l == Yes_Login:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Nice Number,Starting login...')
                Network_Reset()
                Operator_Login()
                l += 1
                content_login = pytesseract.image_to_string(Image.open(r'..\sc_l.png'), lang='chi_sim')
                with open('Result_login.txt', 'wt',encoding="utf-8") as file:
                    file.write('Login Waiting'+str(l)+'_'+content_login)
                Git_push()
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Finish login...')
                gw.getWindowsWithTitle('gnirehtet')[0].close()
                time.sleep(2)
            else:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Wrong login Number')
                
            if n == Yes_Number:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Nice Number,Starting DK...')
                Network_Reset()
                Operate_Phone()
                n += 1
                content_daka = pytesseract.image_to_string(Image.open(r'..\sc_d.png'), lang='chi_sim')
                time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                with open('Result_daka.txt', 'at',encoding="utf-8") as file:
                    file.write(str(time_now)+'Number Waiting'+str(n)+"\r\n"+content_daka+"\r\n"+'Finished...'+'\r\n')
                Git_push()
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Finish DK...')
                gw.getWindowsWithTitle('gnirehtet')[0].close()
                time.sleep(2)
            else:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'Wrong DK Number,waiting...')
            time.sleep(random.randint(268,498))
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'out time waiting...')
            time.sleep(random.randint(450,700))
            continue