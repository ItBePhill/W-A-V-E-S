import time
import sys
x = 0
sleep=0.1

print("------------------BALL.py------------------")
time1=int(input("how long would you like the animation to play"))

               
for count in range(0,time1):
    
    print(" ")
    print("     =====\n    =======\n   =========\n    =======\n     =====")
    time.sleep(sleep)
    print(" ")
    print("    =======\n   =========\n    =======\n     =====")
    time.sleep(sleep)
    print(" ")
    print("   =========\n    =======\n     =====")
    time.sleep(sleep)
    print(" ")
    print("    =======\n     =====")
    time.sleep(sleep)
    print(" ")
    print("     =====")
    time.sleep(sleep)
    print(" ")
    print("    =======\n     =====")
    time.sleep(sleep)
    print(" ")
    print("   =========\n    =======\n     =====")
    time.sleep(sleep)
    print(" ")
    print("    =======\n   =========\n    =======\n     =====")
    time.sleep(sleep)
exec(exec(open("main.py").read()))
sys.exit()

