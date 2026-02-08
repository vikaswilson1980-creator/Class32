class Flashcard():
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + ' ( ' + self.meaning + ' ) '
flash = []
print("Welcome to flashcard application.")
while (True):
    word = input("Enter a name you want to add to a flash card: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(Flashcard(word,meaning))
    option = int(input("Enter 0 if you want to add another flashcard or otherwise enter 1: "))
    if (option):
        break
print("Your flashcard: ")
for i in flash:
    print(" > ",i)
    