import time
from win10toast import *

counter = 0

def loop():
  time.sleep(3600)
  global counter
  counter += 1
  if counter < 2:
    hours = "Hour"
  else:
    hours = "Hours"
  toaster = ToastNotifier()
  toaster.show_toast("Game Reminder", "%s %s Since You Started Playing"%(counter, hours), duration=10)
  loop()

loop()