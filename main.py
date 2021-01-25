import random
import pyautogui
import string
import time


chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# chars = string.printable
chars_list = list(chars)


password = pyautogui.password("Enter a password : ")

guess_password = ""
tic = time.perf_counter()
while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    #print("<======="+ str(guess_password)+ "=======>")

    if(guess_password == list(password)):
        print("\nYour password is : "+ "".join(guess_password))
        break

toc = time.perf_counter()
print(f"Password cracked int in {((toc - tic)/60):0.4f} minutes")