import random
frame0 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
          _        |                                   |                                     |                          |
        /   \      |                                   |                                     |                          |
________\___/______|___________________________________|_____________________________________|__________________________|        
          
          
          
                       """)

frame1 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |      _                            |                                     |                          |
                   |    /   \                          |                                     |                          |
___________________|____\___/__________________________|_____________________________________|__________________________|        
          
          
          
                       """)
frame2 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                               _   |                                     |                          |
                   |                             /   \ |                                     |                          |
___________________|_____________________________\___/_|_____________________________________|__________________________|        
          
          
          
                       """)
frame3 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                                   |             _                       |                          |
                   |                                   |           /   \                     |                          |
___________________|___________________________________|___________\___/_____________________|__________________________|        
          
          
          
                       """) 
frame4 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                                   |                                   _ |                          |
                   |                                   |                                 /   \                          |
___________________|___________________________________|_________________________________\___/__________________________|        
          
          
          
                       """) 
frame5 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                                   |                                     |           _              |
                   |                                   |                                     |         /   \            |
___________________|___________________________________|_____________________________________|_________\___/____________|        
          
          
          
                       """) 

frame6 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                                   |                                     |                          _
                   |                                   |                                     |                        /   \\
___________________|___________________________________|_____________________________________|________________________\___/        
          
          
          
                       """) 
print("pick a difficulty: Expert or Beginner \n Type 'Expert' or 'Beginner'") #User picks their difficulty
difficulty = input()
yourScore = "Your Score: "
score = 0
while(difficulty != "Expert" or difficulty !="Beginner"):
  if(difficulty == "Expert" or difficulty == "Beginner"):
    break
  print("pick a difficulty: Expert or Beginner \n Type 'Expert' or 'Beginner'") # User picks their difficulty
  difficulty = input()
if(difficulty == "Expert"): # If difficulty equals 'Expert' the variable range will be larger
  question1Number1 = random.randint(6,40)
  question1Number2 = random.randint(6,40)
  question2Number1 = random.randint(6,40)
  question2Number2 = random.randint(6,40)
  question3Number1 = random.randint(6,40)
  question3Number2 = random.randint(6,40)
  question4Number1 = random.randint(6,40)
  question4Number2 = random.randint(6,40)
  question5Number1 = random.randint(6,40)
  question5Number2 = random.randint(6,40)
  question6Number1 = random.randint(6,40)
  question6Number2 = random.randint(6,40)
  print(frame0)
  print("Okay, your difficulty level is set to expert. Once you begin you will be prompted to answer various mathmatical questions until your rock as crossed the finsih line.\n Type 'START' to begin.")
elif(difficulty == "Beginner"): # If difficulty equals 'Beginner' the variable range will be smaller
  question1Number1 = random.randint(0,15)
  question1Number2 = random.randint(0,15)
  question2Number1 = random.randint(0,15)
  question2Number2 = random.randint(0,15)
  question3Number1 = random.randint(0,15)
  question3Number2 = random.randint(0,15)
  question4Number1 = random.randint(0,15)
  question4Number2 = random.randint(0,15)
  question5Number1 = random.randint(0,15)
  question5Number2 = random.randint(0,15)
  question6Number1 = random.randint(0,15)
  question6Number2 = random.randint(0,15)
  print(frame0)
  print("Okay, your difficulty level is set to beginner. Once you begin you will be prompted to answer various mathmatical questions until your rock as crossed the finsih line.\n Type 'START' to begin.")
  
start = input() 
if(start == "START"): # User must type 'START' or program will terminate
  userAnswer1 = 0
  answer1 = question1Number1 * question1Number2
  question1 = "What is " + str(question1Number1) + " * " + str(question1Number2) + "?"

  # Question 1
  while(userAnswer1 != answer1): # Program will continue to print the question every time it is answered incorrectly 
    print(question1)
    try:
      userAnswer1 = input()
      userAnswer1 = float(userAnswer1)
    except:
      print("Value entered must be an integer.")
    if(userAnswer1 == answer1): # Chekcs to see if users answer matches actual answer
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(frame1)
      print()
    if(userAnswer1!= answer1):
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(frame0)
      print()

 # Question 2
  userAnswer2 = 0
  answer2 = question2Number1 * question2Number2
  question2 = "What is " + str(question2Number1) + " * " + str(question2Number2) + "?"
  while(userAnswer2 != answer2): # Program will continue to print the question every time it is answered incorrectly 
    print(question2) 
    try:
      userAnswer2 = input()
      userAnswer2 = float(userAnswer2)
    except:
      print("Value entered must be an integer.")
    if(userAnswer2 == answer2): # Chekcs to see if users answer matches actual answer
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(frame2)
      print()
    if(userAnswer2 != answer2):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(frame1)
      print()

  # Question 3
  userAnswer3 = 0
  answer3 = question3Number1 * question3Number2
  question3 = "What is " + str(question3Number1) + " * " + str(question3Number2) + "?"
  while(userAnswer3 != answer3): # Program will continue to print the question every time it is answered incorrectly 
    print(question3) 
    try:
      userAnswer3 = input()
      userAnswer3 = float(userAnswer3)
    except:
      print("Value entered must be an integer.")
    if(userAnswer3 == answer3): # Chekcs to see if users answer matches actual answer
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(frame3)
      print()
    if(userAnswer3 != answer3):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(frame2)
      print()
  
  # Question 4
  userAnswer4 = 0
  answer4 = question4Number1 * question4Number2 + question4Number1
  question4 = "What is " + str(question4Number1) + " * " + str(question4Number2) + " + " + str(question4Number1) + "?"
  while(userAnswer4 != answer4): # Program will continue to print the question every time it is answered incorrectly 
    print(question4)
    try:
      userAnswer4 = input()
      userAnswer4 = float(userAnswer4)
    except:
      print("Value entered must be an integer.")
    if(userAnswer4 == answer4): # Chekcs to see if users answer matches actual answer
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(frame4)
      print()
    if(userAnswer4 != answer4):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(frame3)
      print()
  
  # Question 5
  userAnswer5 = 0
  answer5 = question5Number1 * question5Number2
  question5 = "What is " + str(question5Number1) + " * " + str(question5Number2) + "?"
  while(userAnswer5 != answer5): # Program will continue to print the question every time it is answered incorrectly 
    print(question5)
    try:
      userAnswer5 = input()
      userAnswer5 = float(userAnswer5)
    except:
      print("Value entered must be an integer.")
    if(userAnswer5 == answer5): # Chekcs to see if users answer matches actual answer
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(frame5)
      print()  
    if(userAnswer5 != answer5):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(frame4)
      print()

  # Question 6
  userAnswer6 = 0
  answer6 = question6Number1 * question6Number2 - question6Number2
  question6 = "What is " + str(question6Number1) + " * " + str(question6Number2) + " - " + str(question6Number2) + "?"
  while(question6):  # Program will continue to print the question every time it is answered incorrectly 
    print(question6) 
    try:
      userAnswer6 = input()
      userAnswer6 = float(userAnswer6)
    except:
      print("Value entered must be an integer.")
    if(userAnswer6 == answer6): # Chekcs to see if users answer matches actual answer
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(frame6)
      print()
      print("Your Score: " + str(score))
      print("CONGRATULATIONS!! YOU HAVE COMPLETED THE COURSE.")
      quit()
    if(userAnswer6 != answer6):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(frame5)
      print()
