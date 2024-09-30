# Write a program that takes directory address from users and organize file into corresponding folders using OS module
import os
address=r"C:\Users\sanwa\Desktop\Python 2024\Program\DsPro"
dir = os.listdir(address)
print(dir)
