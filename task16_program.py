def marks():
    mark1 = float(input("Enter your 1st mark: "))
    mark2 = float(input("Enter your 2nd mark: "))
    mark3 = float(input("Enter your 3d mark: "))
    mark4 = float(input("Enter your 4th mark: "))
    mark5 = float(input("Enter your 5th mark: "))
    return mark1, mark2, mark3, mark4, mark5


mark1, mark2, mark3, mark4, mark5 = marks()


def calc_average():
    calc_average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
    return calc_average

def defineLetter(number):
    if number >= 90:
        markLetter = str("A")
    elif 80 <= number < 90:
        markLetter = str("B")
    elif 70 <= number < 79:
        markLetter = str("C")
    elif 60 <= number < 69:
        markLetter = str("D")
    elif number < 60:
        markLetter = str("F")
    return markLetter

average_mark = calc_average()
print("Your average mark is: ", average_mark)

print(mark1, defineLetter(mark1))
print(mark2, defineLetter(mark2))
print(mark3, defineLetter(mark3))
print(mark4, defineLetter(mark4))
print(mark5, defineLetter(mark5))
