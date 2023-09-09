import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

question1 = int(input('How long should the password be?'))

finalpass = ''
for i in range(question1):
    finalpass += random.choice(symbols)
print(finalpass)