import random
import sys
from typing import List, Tuple

# ====================== ASCII ART FRAMES ======================
FRAMES: List[str] = [
    # Frame 0 - Start
    """       
                    _                                   _                                     _                         /|
                   /|\\                                 /|\                                   /|\\                        \|FINISH
                  / | \\                               / | \\                                 / | \\                        |------
           _        |                                   |                                     |                          |
         /   \      |                                   |                                     |                          |
 ________\___/______|___________________________________|_____________________________________|__________________________|        
           
           
                        """,

    # Frame 1
    """       
                    _                                   _                                     _                         /|
                   /|\\                                 /|\                                   /|\\                        \|FINISH
                  / | \\                               / | \\                                 / | \\                        |------
                    |      _                            |                                     |                          |
                    |    /   \                          |                                     |                          |
 ___________________|____\___/__________________________|_____________________________________|__________________________|        
           
           
                        """,

    # Frame 2
    """       
                    _                                   _                                     _                         /|
                   /|\\                                 /|\                                   /|\\                        \|FINISH
                  / | \\                               / | \\                                 / | \\                        |------
                    |                               _   |                                     |                          |
                    |                             /   \ |                                     |                          |
 ___________________|_____________________________\___/_|_____________________________________|__________________________|        
           
           
                        """,

    # Frame 3
    """       
                    _                                   _                                     _                         /|
                   /|\\                                 /|\                                   /|\\                        \|FINISH
                  / | \\                               / | \\                                 / | \\                        |------
                    |                                   |             _                       |                          |
                    |                                   |           /   \                     |                          |
 ___________________|___________________________________|___________\___/_____________________|__________________________|        
           
           
                        """,

    # Frame 4
    """       
                    _                                   _                                     _                         /|
                   /|\\                                 /|\                                   /|\\                        \|FINISH
                  / | \\                               / | \\                                 / | \\                        |------
                    |                                   |                                   _ |                          |
                    |                                   |                                 /   \                          |
 ___________________|___________________________________|_________________________________\___/__________________________|        
           
           
                        """,

    # Frame 5
    """       
                    _                                   _                                     _                         /|
                   /|\\                                 /|\                                   /|\\                        \|FINISH
                  / | \\                               / | \\                                 / | \\                        |------
                    |                                   |                                     |           _              |
                    |                                   |                                     |         /   \            |
 ___________________|___________________________________|_____________________________________|_________\___/____________|        
           
           
                        """,

    # Frame 6 - Finish
    """       
                    _                                   _                                     _                         /|
                   /|\\                                 /|\                                   /|\\                        \|FINISH
                  / | \\                               / | \\                                 / | \\                        |------
                    |                                   |                                     |                          _
                    |                                   |                                     |                        /   \\
 ___________________|___________________________________|_____________________________________|________________________\___/        
           
           
                        """
]

def clear_screen() -> None:
    """Clear the terminal screen."""
    print("\033c", end="")


def get_difficulty() -> Tuple[int, int]:
    """Get difficulty level from user."""
    print("=== ROCK RACER ===\n")
    print("Pick a difficulty: Expert or Beginner")
    
    while True:
        choice = input("> ").strip().lower()
        if choice == "expert":
            return (6, 40)
        elif choice == "beginner":
            return (0, 15)
        print("Please type 'Expert' or 'Beginner'.")


def generate_questions(min_val: int, max_val: int) -> List[Tuple[str, int]]:
    """Generate 6 questions with their correct answers."""
    questions = []
    
    patterns = [
        lambda: (a := random.randint(min_val, max_val),
                b := random.randint(min_val, max_val),
                f"What is {a} * {b}?", a * b),
        
        lambda: (a := random.randint(min_val, max_val),
                b := random.randint(min_val, max_val),
                f"What is {a} * {b} + {a}?", a * b + a),
        
        lambda: (a := random.randint(min_val, max_val),
                b := random.randint(min_val, max_val),
                f"What is {a} * {b} - {b}?", a * b - b),
    ]
    
    for _ in range(6):
        _, _, q_text, answer = random.choice(patterns)()
        questions.append((q_text, answer))
    
    return questions


def main() -> None:
    diff_range = get_difficulty()
    min_val, max_val = diff_range
    
    questions = generate_questions(min_val, max_val)
    score = 0
    current_frame = 0
    
    clear_screen()
    print(FRAMES[0])
    print(f"\nYour difficulty is set to {'Expert' if min_val == 6 else 'Beginner'}.")
    input("\nType 'START' to begin... ")
    
    clear_screen()
    
    for i, (q_text, correct) in enumerate(questions, 1):
        print(f"\n--- Question {i}/6 ---")
        
        while True:
            print(q_text)
            try:
                user_input = input("> ").strip()
                user_answer = float(user_input)
                
                score += 1
                
                if abs(user_answer - correct) < 0.001:  # Allow small float tolerance
                    print("Correct! <--ADVANCED-->\n")
                    current_frame += 1
                    print(FRAMES[current_frame])
                    break
                else:
                    print("Incorrect! <--STAY-->\n")
                    print(FRAMES[current_frame])
                    
            except ValueError:
                print("Please enter a valid number.\n")
                score += 1  # Penalty for invalid input
    
    # Final screen
    clear_screen()
    print(FRAMES[6])
    print("\n CONGRATULATIONS! You crossed the finish line!")
    print(f"Final Score: {score}/6")
    print("   (Lower is better. Perfect score is 6)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThanks for playing Rock Racer!")
        sys.exit(0)
