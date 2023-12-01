
#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number:d} is {digit:d} and is", end -" ") 
if last_num > 5:
    print(f"is greater than 5")
elif last_num == 0:
    print(f"0")
else:
    print(f" less than 6 and not 0")
