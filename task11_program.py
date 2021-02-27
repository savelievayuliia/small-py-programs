import random

SUM1 = 247

def numbers():
    number1 = random.randint(1, SUM1)
    number2 = SUM1 - number1
    return number1, number2


number1, number2 = numbers()
print(number1)
print(number2)
