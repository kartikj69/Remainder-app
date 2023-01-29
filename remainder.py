import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="All Day Reminder",
            message="Today Ihave to sumbit my assignment",
            timeout=20
        )
        time.sleep(60*60)
#  if you want to run in the background, use "pythonw .\remainder.py"
