from random import choice

questions = ["Why the sky is blue?: ",
             "Where are the dianousors?: ",
             "Why the banana is color yellow?: "]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()


print("Oh....Okay!")
    
    
