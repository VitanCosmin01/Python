# pip install plyer
import time

from asgiref.timeout import timeout
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT",
            message="Take a break! It has been two minutes!",
            timeout=10
        )
        time.sleep(120)
