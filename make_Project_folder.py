import time,os
def CMD(command):
    os.system(command)
    time.sleep(0.2)
print('Nasa.zhang@20220515\r\n')
print('eg:"D:" or "D:\\\project"')
diskname = input('输入要在哪个目录创建项目并回车：')
print('\r\n')
print('eg:P840')
projectname = input('输入要创建的项目名并回车：')

path = diskname+'\\'+projectname+'\\'+projectname
filename = ('_00_BuJu','_01_OD','_02_BlockDiagram','_03_SCH_PCB_BOM','_04_DataSheet','_05_LinkBudget','_06_SignalPath','_07_BringUp','_08_CalNST','_09_TestReport','_10_Desense','_11_FuPan',)
for key in filename:
    outcome = path+key
    print('已生成：'+outcome)
    CMD('md '+outcome)