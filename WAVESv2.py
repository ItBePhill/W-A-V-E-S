import time
import sys
print("-------------WAVESv2.py------------")
x = int(input("how long would you like the animation to play"))
ans=input("= ")
wait = float(input("(lower = faster, default = 0.2)Wave Speed = "))
num = 0


for i in range(0, x):
  num+=1
  print(num," ",ans)
  time.sleep(wait)
  num+=1
  print(num,"  ",ans)
  time.sleep(wait)
  num+=1
  print(num,"   ",ans)
  time.sleep(wait)
  num+=1
  print(num,"    ",ans)
  time.sleep(wait)
  num+=1
  print(num,"   ",ans)
  time.sleep(wait)
  num+=1
  print(num,"  ",ans)
  time.sleep(wait)
  num+=1
  print(num," ",ans)
exec(open("main.py").read())
sys.exit()
  

  
  