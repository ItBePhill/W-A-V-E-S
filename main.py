import time
import sys
print("------------------main.py------------------")
ans = input("which would you like to open?")



if ans == "exit" or ans == "quit":
  print("\rQuitting.", end = "")
  time.sleep(0.7)
  print("\rQuitting..", end = "")
  time.sleep(0.7)
  print("\rQuitting... \n", end = "")
  sys.exit()

elif ans == "ball":
  print("opening BALL.py")
  print("\r.",end="")
  time.sleep(0.5)
  print("\r..",end="")
  time.sleep(0.5)
  print("\r... \n",end="")
  time.sleep(0.5)
  exec(open("BALL.py").read())

elif ans == "bounce":
  print("opening BOUNCE.py")
  print("\r.",end="")
  time.sleep(0.5)
  print("\r..",end="")
  time.sleep(0.5)
  print("\r... \n",end="")
  time.sleep(0.5)
  exec(open("BOUNCE.py").read())

elif ans == "bounce2":
  print("opening BOUNCEv2.py")
  print("\r.",end="")
  time.sleep(0.5)
  print("\r..",end="")
  time.sleep(0.5)
  print("\r... \n",end="")
  time.sleep(0.5)
  exec(open("BOUNCEv2.py").read())

elif ans == "waves":
  print("opening WAVES.py")
  print("\r.",end="")
  time.sleep(0.5)
  print("\r..",end="")
  time.sleep(0.5)
  print("\r... \n",end="")
  time.sleep(0.5)
  exec(open("WAVES.py").read())
  
elif ans == "waves":
  print("opening WAVES.py")
  print("\r.",end="")
  time.sleep(0.5)
  print("\r..",end="")
  time.sleep(0.5)
  print("\r... \n",end="")
  time.sleep(0.5)
  exec(open("WAVES.py").read())
  
elif ans == "waves2":
  print("opening WAVESv2.py")
  print("\r.",end="")
  time.sleep(0.5)
  print("\r..",end="")
  time.sleep(0.5)
  print("\r... \n",end="")
  time.sleep(0.5)
  exec(open("WAVESv2.py").read())
  
  
else:
  print("error: invalid input")
  exec(open("main.py").read())