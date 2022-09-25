# Create simple timer, for 1 minute. Once 1 minute will past - print "It's time!"
# Advanced - every minute print message "Repeat a task".
from datetime import datetime, timedelta

expected_datetime = datetime.now() + timedelta(seconds=10)

while True:
    if datetime.now() > expected_datetime:
        print('test')
        expected_datetime = datetime.now() + timedelta(seconds=10)