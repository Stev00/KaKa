#!/usr/bin/env python
# _*_ coding:utf-8 _*_
 
# 使用正则表达式筛选设备 id
import re
# 使用 os 模块调用命令
import os
 
# app包名称，不包含.apk  注意名字大小写
appName = "wework"
# 读取设备 id
read_DeviceId = list(os.popen('adb devices').readlines())
'''执行cmd命令，将结果保存为列表read_DeviceId '''
 
device_Id = read_DeviceId[1].split('\t')[0]
'''取列表中的第二项，进行字符串切分，切分后的列表取第一项
此处有个问题，若有多个设备连入，则只能处理第一个
此处看可用正则实现？
'''
print("deviceID: " + device_Id)
 
# 读取设备系统版本号
device_Android_Version = list(os.popen('adb shell getprop ro.build.version.release').readlines())
device_Android_VersionSdk = list(os.popen('adb shell getprop ro.build.version.sdk').readlines())
device_Version = device_Android_Version[0].split('\n')[0]
device_VersionSdk = device_Android_VersionSdk[0].split('\n')[0]
print("Version: " + device_Version)
print("platformVersion: " + device_VersionSdk)
 
 
packageName = list(os.popen('adb shell pm list packages -e \"'+appName+'\"').readlines())
print(packageName)
packageName=packageName[0].strip().split(':')[1]
print("package: "+packageName)
 
 
# 读取 APK 的 package 信息
appPackageAdb = list(os.popen('adb shell dumpsys package ' + packageName).readlines())
length = len(appPackageAdb)
for index in range(length):
    if appPackageAdb[index].find("Non-Data") != -1:
        packageInfo = appPackageAdb[index + 2].strip()
        matchObj = re.match(r'.* (.*)/(.*?) .*', packageInfo, re.M | re.I)
        if matchObj:
            print("appActivity:", matchObj.group(2))
        break;