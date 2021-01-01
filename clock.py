from datetime import datetime
from time import sleep
import os

def _correct_time(time):
    return time if len(str(time)) > 1 else f"0{time}"

def start():
    os.system('cls')
    while True:
        clock = datetime.now()
        hour = _correct_time(clock.hour)
        minute = _correct_time(clock.minute)
        second = _correct_time(clock.second)
        
        print(f'{hour}:{minute}:{second}')
        sleep(1)
        os.system('cls')
