import os
import time
import sys

time.sleep(1)
os.system('clear')

print("\033[1;32;40m  ")
os.system("figlet VIRANK")
print("  Developer: S4RT-4K")
print("  VERSION: 1.0")
print(" ")
First_name = input("\033[1;32;40m Your First Name:- ")

if len(First_name) == 0:
 print(" ")
 print("Please Enter Your First Name")
 print(" ")
 sys.exit()

print(" ")
Last_name = input(" Your Last Name:-  ")

if len(Last_name) == 0:
 print(" ")
 print("Please Enter Your Last Name")
 print(" ")
 sys.exit()
time.sleep(1)

print(" ")
print("Is This Name Correct?" + " " + First_name.upper() + " " + Last_name.upper())
print(" ")
time.sleep(1)

correct = input("If It Is Correct Then Type y Otherwise n: ")
time.sleep(1)
print(" ")
if correct == "y" or "Y":
 print("OK! Let's Move On")
else:
 print("Sad! Run It Again With Correct Information")
 print(" ")
 sys.exit()

time.sleep(2)
print(" ")
os.system("cd /sdcard && wget -nd -H -p -A jpg -e robots=off  https://ibb.co/6WRVMZx")
os.system('clear')
for i in range(100):
 time.sleep(0.1)
 print("\033[1;33;40m Your System is Hacked, SpywareID#~SPY70D, Gaining Data...Sending to the Database")

os.system('clear')
for j in reversed(range(11)):
 time.sleep(1)
 print(f"\033[1;34;40m Gaining Data Succeeded, Turning Off Computer In {j} seconds.")

os.system('clear')

for l in range(11):
 time.sleep(0.3)
 print("\033[1;31;40m PRANKED SUCCESSFULLY HEHE :-)")
