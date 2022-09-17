import random as rn
import time

print('Multiplication Tutor')

# Aim: create application to practice multiplication tables


def MathTutor():
    # count correct and incorrect answers
    correct = 0
    wrong = 0

    # Range of numbers the user would like to multiply by
    rainge = int(
        input('What is the biggest number you would like to multiply by?'))

    # how many equations would user like to solve
    eqns = int(input('How many problems would you like to solve? '))
    timed = []
    mul1, mul2, ans = [], [], []
    # generate maths problems and collect user answer
    for i in range(eqns):
        rand1, rand2 = int(rn.uniform(1, rainge)), int(rn.uniform(1, rainge))

        # measure user time to answer
        start = time.time()
        answer = int(input(f'What is {rand1} * {rand2}?: '))
        end = time.time()
        elapsed = end - start
        timed.append(round(elapsed, 1))
        total_time = sum(timed)

        # save questions and answers
        mul1.append(rand1)
        mul2.append(rand2)
        ans.append(answer)
        quest = list(zip(mul1, mul2, ans))
        # Test if user answer is correct
        if answer != rand1*rand2:
            print('Incorrect')
            wrong = wrong + 1
        elif answer == rand1*rand2:
            print('Correct')
            correct = correct + 1
    # Return the questions answered and the time taken to answer
    for i in range(eqns):
        print(f'Question {i+1}: {mul1[i]} * {mul2[i]} = {mul1[i]*mul2[i]}.\n You answered: {ans[i]}.\n',
              f'It took you {timed[i]} seconds to answer this question')
    # Return the accuracy of answers.
    return print(f'You got {correct} correct out of {eqns} questions. You have an accuracy of {round(((correct)/eqns)*100, 0)}%. Thank you for playing.',)


MathTutor()
