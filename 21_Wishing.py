# Program for wishing according to time.

import time

hours = time.localtime().tm_hour

if hours < 12:
    print("Good Morning")

elif hours < 17:
    print("Good Afternoon")

elif hours < 21:
    print("Good Evening")

else:
    print("Good Night")