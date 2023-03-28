import os

import numpy as np
import pandas as pd

pwd = os.getcwd()

# tell the user how to quit the program then clear the screen
print("Press 'q' to quit the program")
# wait for user input to continue
input("Press Enter to continue...")
# clear screen for next question
os.system('cls' if os.name == 'nt' else 'clear')

# ask the user what test he wants to take
print("1. Etapa 2 2022")
print("2. Finala 2022")
test = input("Select a test: ")
url = ""
if test == '1':
    # pull the csv file from github
    url = 'https://gist.githubusercontent.com/Andrei9383/6ac89a97adfb10e31e244ef84821ec3c/raw/56cbe1fc5bef6f1bbb654d28ac5ff6cb22f57160/AsusChallenge2022_Etapa2.csv'
else:
    # pull the csv file from github
    url = 'https://gist.githubusercontent.com/Andrei9383/781e8b14c8a116d336c8376110c1a1b5/raw/e3fa75dc819b42dfd6ad5e9b9c9776e62d56798e/AsusChallenge2022_Finala.csv'

os.system('cls' if os.name == 'nt' else 'clear')

dataset = pd.read_csv(url)
#dataset = pd.read_csv(pwd + '/editedEtapa2.csv')

# get every row from the second column and put it in a list
list = dataset.iloc[:, 1].values

# get every column from the third to the sixth, inclusive and put them grouped by 4 in a list
list2 = dataset.iloc[:, 2:6].values

# get every row from the last column and put it in a list
list3 = dataset.iloc[:, -1].values

rightAnswers = 0
wrongAnswers = 0

options = ['a', 'b', 'c', 'd']
for index, question in enumerate(list):
    # print the question in bold text
    print("\033[0m" + str(index + 1) + "/" + str(len(list)) + ") " + "\033[1m" + question + "\033[0m")
    print('\n')
    for optionIndex, option in enumerate(options):
        # check for nan
        if not pd.isnull(list2[index][optionIndex]):
            # print the answers in bold text, without the a, b, c or d in normal text
            print("\033[0m" + option + ") " + "\033[1m" + list2[index][optionIndex])
    print('\n')
    # get user input, expects A, B, C or D
    answer = input("Answer: ")
    # check if the user wants to quit
    if answer == 'q':
        break
    # check if answer is valid
    if answer not in options:
        print("Invalid answer")
        print('\n')
        continue
    # check if answer is correct
    if list2[index][options.index(answer)] == list3[index]:
        # print Correct in green color and bold text
        print("\033[92m \033[1m Correct \033[0m")
        rightAnswers += 1
    else:
        # print Wrong in red color and bold text
        print("\033[91m \033[1m Wrong \033[0m")
        # print the correct answer
        print("Correct answer: " + list3[index])
        wrongAnswers += 1
    print('\n')
    # wait for user input to continue
    input("Press Enter to continue...")
    # clear screen for next question
    os.system('cls' if os.name == 'nt' else 'clear')

# print the right answers in green color and the wrong answers in red color
print("\033[92m Right answers: " + str(rightAnswers) + "\033[0m")
print("\033[91m Wrong answers: " + str(wrongAnswers) + "\033[0m")

# print the percentage of right answers and the percentage of wrong answers, with only two decimal places
print("\033[92m Percentage of right answers: " + str(round(rightAnswers / (rightAnswers + wrongAnswers) * 100, 2)) + "% \033[0m")
print("\033[91m Percentage of wrong answers: " + str(round(wrongAnswers / (rightAnswers + wrongAnswers) * 100, 2)) + "% \033[0m")

# print the total number of questions
print("Total questions: " + str(rightAnswers + wrongAnswers))

# ask the user if he wants to see all the questions with answers
print("Do you want to see all the questions with answers? (y/n)")

answer = input("Answer: ")
if answer == 'y':
    # print all the questions with answers
    for index, question in enumerate(list):
        print("\033[0m" + str(index + 1) + ") " + "\033[1m" + question + "\033[0m")
        print('\n')
        for optionIndex, option in enumerate(options):
            # check for nan
            if not pd.isnull(list2[index][optionIndex]):
                # print the answers in bold text, without the a, b, c or d in normal text
                print("\033[0m" + option + ") " + "\033[1m" + list2[index][optionIndex])
        print('\n')
        # print the correct answer
        print("Correct answer: " + list3[index])
        print('\n')
else:
    exit()
