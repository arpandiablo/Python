import random
list_questions = ['Who was the legendary Benedictine monk who invented champagne?','Where was the origin of the sport badminton?','What is the name of the longest river in the world?','In the Solar System, which is the hottest planet?','When was Alaska sold to the United States?']
list_answers = ['Dom Perignon','Pune','Nile','Venus','1867']
print('What is your name: ')
name = input()
while True:
    question = random.choice(list_questions)
    print(question)
    answer=input()
    if answer not in list_answers:
        break
    elif list_answers.index(answer) == list_questions.index(question):
        print('Congratulations!, Now next question')
    else:
        break
print('Sorry but the answer is incorrect. Thanks for playing ', name)