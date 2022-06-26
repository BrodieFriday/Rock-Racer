

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

print("pick a difficulty: Expert or Beginner \n Type 'Expert' or 'Beginner'")
difficulty = input()
score = 0
if(difficulty == "Expert"):
  print("Okay, your difficulty level is set. Once you begin you will be prompted to answer various mathmatical questions until your rock as crossed the finsih line.\n Type 'START' to begin.")
  start = input()
  if(start == "START"):
    print("What is 2 + 2")
    correctAnswer = 4
    try:
      answer1 = input()
      answer1 = float(answer1)
    except:
      print("Value entered must be an integer.")
  while(answer1 != correctAnswer):
    print(P0)
    print("Incorrect! <--STAY-->")
    print()
    print("What is 2 + 2?")
    try:
      answer1 = input()
      answer1 = float(answer1)
    except:
      print("Value entered must be an integer.") 
  if(answer1 == correctAnswer):
    score =  score + 1
    print(P1)
    print("Correct! <--ADVANCED-->")
    print()
    





print(score)