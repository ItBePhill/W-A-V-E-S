import time
import random
import sys
print("------------------BOUNCEv2.py------------------")
x = int(input("how long would you like the animation to play"))
c = 0
sleep=0.08
rand = int(input("Max random number?"))
num = random.randint(0,rand)
for i in range(0, x):
    
    print("c                                                                                    ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("c                                                                                      ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("3                                                                                       ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("4                                                                                         ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("5                                                                                         ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("6                                                                                          ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("7                                                                                         ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("8                                                                                         ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("9                                                                                       ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("10                                                                                    ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("11                                                                                   ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
    print("12                                                                                 ",num)
    time.sleep(sleep)
    num = random.randint(0,rand)
    c = c +1
exec(open("main.py").read())
sys.exit()
    
    
   
