# gemaakt door ofek
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{}<>:;,.?!@#$%^&*_+"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols


length = int(input("Wachtwoordlengte: "))
amount = int(input("Aantal wachtwoorden: "))
password = ""

for x in range(amount):
    password = "".join(random.choice(all) for i in range(length))
    print(password)


input('Druk op ENTER om af te sluiten.')
