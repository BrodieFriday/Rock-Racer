

P0 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
          _        |                                   |                                     |                          |
        /   \      |                                   |                                     |                          |
________\___/______|___________________________________|_____________________________________|__________________________|        
          
          
          
                       """)

P1 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |      _                            |                                     |                          |
                   |    /   \                          |                                     |                          |
___________________|____\___/__________________________|_____________________________________|__________________________|        
          
          
          
                       """)
P2 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                               _   |                                     |                          |
                   |                             /   \ |                                     |                          |
___________________|_____________________________\___/_|_____________________________________|__________________________|        
          
          
          
                       """)
P3 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                                   |             _                       |                          |
                   |                                   |           /   \                     |                          |
___________________|___________________________________|___________\___/_____________________|__________________________|        
          
          
          
                       """) 
P4 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                                   |                                   _ |                          |
                   |                                   |                                 /   \                          |
___________________|___________________________________|_________________________________\___/__________________________|        
          
          
          
                       """) 
P5 = ("""       
                   _                                   _                                     _                         /|
                  /|\\                                 /|\                                   /|\\                        \|FINISH
                 / | \\                               / | \\                                 / | \\                        |------
                   |                                   |                                     |           _              |
                   |                                   |                                     |         /   \            |
___________________|___________________________________|_____________________________________|_________\___/____________|        
          
          
          
                       """) 

P6 = ("""       
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
if(difficulty == "Expert"):
  print(P0)
  print("Okay, your difficulty level is set. Once you begin you will be prompted to answer various mathmatical questions until your rock as crossed the finsih line.\n Type 'START' to begin.")
  start = input()
  if(start == "START"):
    userAnswer1 = 0
    answer1 = 4
    # Question 1
    while(userAnswer1 != answer1):
      print("What is 2 + 2?")
      try:
        userAnswer1 = input()
        userAnswer1 = float(userAnswer1)
      except:
        print("Value entered must be an integer.")
      if(userAnswer1 == answer1):
        score = score + 1
        print()
        print(yourScore + str(score))
        print("Correct! <--ADVANCED-->")
        print(P1)
        print()
      if(userAnswer1!= answer1):
        score = score + 1
        print()
        print(yourScore + str(score))
        print("Incorrect! <--STAY-->")
        print(P0)
        print()
    

 # Question 2
  answer2 = 8
  userAnswer2 = 0
  while(userAnswer2 != answer2):
    print("What is 4 + 4?") # Question 2
    try:
      userAnswer2 = input()
      userAnswer2 = float(userAnswer2)
    except:
      print("Value entered must be an integer.")
    if(userAnswer2 == answer2):
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(P2)
      print()
    if(userAnswer2 != answer2):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(P1)
      print()

  # Question 3
  answer3 = 16
  userAnswer3 = 0
  while(userAnswer3 != answer3):
    print("What is 8 + 8?") # Question 2
    try:
      userAnswer3 = input()
      userAnswer3 = float(userAnswer3)
    except:
      print("Value entered must be an integer.")
    if(userAnswer3 == answer3):
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(P3)
      print()
    if(userAnswer3 != answer3):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(P2)
      print()
  

  # Question 4
  answer4 = 20
  userAnswer4 = 0
  while(userAnswer4 != answer4):
    print("What is 10 + 10?") # Question 2
    try:
      userAnswer4 = input()
      userAnswer4 = float(userAnswer4)
    except:
      print("Value entered must be an integer.")
    if(userAnswer4 == answer4):
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(P4)
      print()
    if(userAnswer4 != answer4):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(P3)
      print()
  

  # Question 5
  answer5 = 30
  userAnswer5 = 0
  while(userAnswer5 != answer5):
    print("What is 15 + 15?") # Question 2
    try:
      userAnswer5 = input()
      userAnswer5 = float(userAnswer5)
    except:
      print("Value entered must be an integer.")
    if(userAnswer5 == answer5):
      score = score + 1
      print()
      print(yourScore + str(score))
      print("Correct! <--ADVANCED-->")
      print(P5)
      print()  
    if(userAnswer5 != answer5):
      score = score + 1
      print(yourScore + str(score))
      print("Incorrect! <--STAY-->")
      print(P4)
      print()

print("Your Score: " + str(score))