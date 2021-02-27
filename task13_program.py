
def getting_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the first number: "))
    return num1, num2

num1 , num2 = getting_numbers()
if num1 >= num2:
    print(num1)
elif num2 >= num1:
    print(num2)
