import pyautogui
import time

msg = input("your message: ")
n = input("How many times do you want to send Your message?  ")

count = 5
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("BooooM!!!")

for i in range(0,int(n)):
    pyautogui.typewrite(msg + '\n')