'''
██╗███╗░░░███╗██████╗░░█████╗░██████╗░████████╗░██████╗
██║████╗░████║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║██╔████╔██║██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░
██║██║╚██╔╝██║██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗
██║██║░╚═╝░██║██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝
╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
'''

from time import sleep
import random
from clear import clear, tokenvalue


'''
██╗░░░██╗░█████╗░██████╗░██╗██████╗░██╗░░░░░███████╗░██████╗
██║░░░██║██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔════╝██╔════╝
╚██╗░██╔╝███████║██████╔╝██║██████╦╝██║░░░░░█████╗░░╚█████╗░
░╚████╔╝░██╔══██║██╔══██╗██║██╔══██╗██║░░░░░██╔══╝░░░╚═══██╗
░░╚██╔╝░░██║░░██║██║░░██║██║██████╦╝███████╗███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚══════╝╚═════╝░
'''

questionfile = "question.txt" #What file should the question be taken from?
token = 00000000




'''
░█████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██║░░██║█████╗░░
██║░░██╗██║░░██║██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝
'''

score = 0
questionnum = 0
question_list = list()
if token != tokenvalue:
    print("INCORRECT TOKEN")
    print("Your token should be " + str(tokenvalue))


with open(questionfile, "r") as f:
    lines = f.readlines()

    for line in lines:
        q_a = line.split('|.|')
        question = q_a[0].strip()
        answer = q_a[1].strip()
        question_list.append((question, answer))

while True:
    questionnum = questionnum + 1
    q_idx = random.randint(0, len(question_list) - 1)
    this_question = question_list[q_idx][0]
    this_answer = question_list[q_idx][1]
    your_answer = input(this_question + "   ") 
    if your_answer == "exit":
        print()
        print("Exited.")
        print()
        break
    elif your_answer == this_answer:
        print()
        print('Correct.')
        score = score + 1
        print()
    else:
        print()
        print("Wrong! It is " + this_answer + ".")
        print()
    sleep(2)
    clear()
    print("Question: " + str(questionnum))
    print("Your Score: " + str(score))
    print()
    print()
    print()