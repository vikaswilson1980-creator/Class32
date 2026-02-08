import random
class Fruit():
    def __init__(self):
        self.fruit = {"apple":"Red","orange":"Orange","watermelon":"Green","banana":"Yellow"}
    def quiz(self):
        while(True):
            fruit,color = random.choice(list(self.fruit.items()))
            print("What is the color of {}:".format(fruit))
            user_answer = input()
            if user_answer.lower() == color.lower():
                print("Correct Answer")
            else:
                print("Wrong Answer")
            option = int(input("Enter 0 if you want to play again or otherwise enter 1: "))
            if (option):
                break
print("Welcome to fruit quiz")
fq = Fruit()
fq.quiz()
