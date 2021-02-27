correct_list = ["W", "B", "A", "C", "M", "C", "R", "B", "F", "D", "C", "B", "A", "C", "A", "D", "Q", "B", "D", "A"]


def getting_answers():
    answers = []
    infile = open('student_solution.txt', 'r')
    answers = infile.read().splitlines()
    infile.close()
    # print(answers)
    return answers


def answers_validation(x, y):
    if x == y:
        print("You've passed test")
    else:
        print("You haven't passed test")


# answers_validation(correct_list, getting_answers())

def points_calc():
    sum_points = 0
    i = 0
    incorrect_answers = []
    while i != 20:
        if correct_list[i] == getting_answers()[i]:
            sum_points += 1
            i += 1
        else:
            sum_points += 0
            i += 1
            incorrect_answers.append(i)
    if sum_points >= 15:
        print("You've got ", sum_points, " points")
        print("You've passed the test")
    else:
        print("You have wrong answers in: ", incorrect_answers)

points_calc()
