import time
import random
import sys
print("------------------BOUNCE.py------------------")
x = int(input("how long would you like the animation to play"))
c = 0
sleep=0.08
rand = 100000
num = random.randint(0,rand)
for i in range(0, x):
    print("    ---------   ")
    time.sleep(sleep)
    print("   -----------  ")
    time.sleep(sleep)
    print("  -------------  ")
    time.sleep(sleep)
    print(" ---------------  ")
    time.sleep(sleep)
    print("-----------------")
    time.sleep(sleep)
    print("-----------------")
    time.sleep(sleep)
    print(" ---------------  ")
    time.sleep(sleep)
    print("  -------------  ")
    time.sleep(sleep)
    print("   -----------  ")
    time.sleep(sleep)
    print("    ---------   ")
    time.sleep(sleep)
exec(open("main.py").read())
sys.exit()
  
     


    
