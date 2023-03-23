try:
    from time import sleep,time
    from pyautogui import click
    from pynput.mouse import Listener,Button
    from datetime import datetime as dt
    import os
except ImportError:
    print('>>未安装一些包,即将安装')
    if os.popen('pip -V').read().split('\\')[1][:-2] == 'Python3':
        os.popen('pip3 install keyboard pyautogui -i https://pypi.tuna/tsinghua.edu.cn/simple')
        print('>>完成后请重启脚本...')
    else :print('>>未知错误,联系发布者.')

def file_add(file,content):
    with open(file,'a') as f:f.write(content)
def on_click(x,y,btn,pressed):
    if btn == Button.left :
        print('{0} 在 {1} 用时 {2}'.format('按下' if pressed else '释放',(x,y),time()))
        file_add('events',f'{x},{y},{time()},' if pressed else '')
    else:
        print('>>您键入了右键,已结束...\n>>重新运行以使用!')
        return False
def record():
    mouse_listener = Listener(on_click=on_click)
    mouse_listener.start()
    mouse_listener.join()
def replay(evnt):
    print(f'>>到达预定时间: {dt.now()}')
    for i in range(len(evnt)//3):
        print(f'>>尝试复现点击 {evnt[i*3]},{evnt[i*3+1]}')
        click(int(evnt[i*3]),int(evnt[i*3+1]))
        try:sleep(float(evnt[i*3+5])-float(evnt[i*3+2]))
        except IndexError:pass
    print('>>复现完成,可以关闭!')

print('>>此脚本由YGL编写 1316171511@qq.com\n\
>>如果没有录制过鼠标事件,会生成events文件,有则直接设定时间\n\
>>脚本无删除录像的若要删除动作,请删除同文件夹下events文件\n\
>>执行过程中将在你指定的日期复现录制的动作,但一定注意格式\n\
>>录制时脚本只记录鼠标左键点击,复现过程是包含间隔时间的!\n\
>>鼠标移动到屏幕四角会触发保险,强制退出,请注意这一点...\n')
try:f = open('events')
except FileNotFoundError:
    with open('events','w') : print('>>没有日志文件,已创建...\n')
with open('events') as f:
    if f.read() == '':
        print('>>没有鼠标事件记录,将开始记录,右键结束录制...')
        record()
evnt = []
with open('events')as f : evnt = f.read().split(',')[:-1]
while evnt:
    d = input('\n>>开始计时任务,请输入预定时间  格式: 年/月/日/时/分(个位数用前面加0):')
    print(f'>>设定于 : {d} 开始,请勿关闭脚本...')
    if dt.now().strftime('%Y-%m-%d %H:%M')>d :
        print('>>当前时间已经超过指定日期,需要重新设置:')
        continue
    while dt.now().strftime('%Y/%m/%d/%H/%M')<d : sleep(20)
    replay(evnt)
    break
print("test message")