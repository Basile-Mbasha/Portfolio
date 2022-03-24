#-user: Basile M.
#-Date: March 23rd,2022  10:11PM
#- digital clock in Python


import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="\n", flush=True)
  time.sleep(1)

# happy_coding,...
