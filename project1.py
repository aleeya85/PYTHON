import time
print("--------------------------------------------------")
#Welcome the user
print("Welcome to the Music Quiz Game!")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) WHO IS THE CREATOR OF ARJUNA BETA SONG?\n(A) Fynn Jamal\n(B) P.Ramlee\n(C) Siti Nurhaliza\n(D) Sudirman Arshad\n\n")
answer_1= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)MOST XPDC SONGS ARE GENRE?\n(A) Pop Music\n(B) Jazz\n(C) Rock\n(D) Disco\n\n")  
answer_2 = "c"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  WHO IS THE CREATOR OF LEMON TREE?\n(A) Dua Lipa\n(B) Bebe Rexha\n(C) Camila\n(D) Fools Garden\n\n")
answer_3= "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  WHO IS THE CREATOR OF SHE'S GONE?\n(A) SteelHeart\n(B) Clivia Rodrigo\n(C) Justin Bieber\n(D) Camila\n\n")
answer_4= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  WHO IS THE CREATOR OF SACRIFICE?\n(A) Miley Cyrus\n(B) Elton John\n(C) Zara Larsson\n(D) Olly Murs\n\n")
answer_5= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("well done! Your Score was", score)
    break

while score <2:
    print("Better luck next time! Your score was",score)
    break

#Goobye message
print("Thank you for playing the Music Quiz Game!")
