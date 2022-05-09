import pyautogui,time,datetime,ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

def main():
    print("Start.")
    n=1
    start_time_am = '08:55:00'
    end_time_am =  '09:09:59'
    start_time_pm = '17:50:00'
    end_time_pm =  '18:10:59'
    pyautogui.FAILSAFE = False
    while True:
        xingqi = datetime.datetime.now().weekday() + 1
        now_localtime = time.strftime("%H:%M:%S", time.localtime())	
        if start_time_am < now_localtime < end_time_am and 1 <= xingqi <= 5:
            x1,y1 = pyautogui.position()
            time.sleep(30)
            x2,y2 = pyautogui.position()
            if x1-x2 == 0 and y1-y2 == 0:
                pyautogui.press('up')
                if n%20==0:
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                n+=1
        elif start_time_pm < now_localtime < end_time_pm and 1 <= xingqi <= 5:
            x1,y1 = pyautogui.position()
            time.sleep(30)
            x2,y2 = pyautogui.position()
            if x1-x2 == 0 and y1-y2 == 0:
                pyautogui.press('up')
                if n%20==0:
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                n+=1
            else:
                if n%20==0:
                    print('.')
                n+=1
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'waiting time...')
            time.sleep(300)
            continue
if __name__ == '__main__':
    main()