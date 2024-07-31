import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"
length=int(input("enter length:"))
password=""

for a in range (length):
    password=password+random.choice(chars)
print (password)

