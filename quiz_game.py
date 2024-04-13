import random

def ask_question(question, correct_answer):
    global score  # Use the global score variable
    answer = input(question)  # Get the user's answer
    if answer.lower() == correct_answer.lower():
        print('Correct!')
        score += 1  # Increase the score for a correct answer
    else:
        print(f"Incorrect! The correct answer was {correct_answer}.")
    print(f"Your current score is: {score}/{total_questions}")

# Welcome message for the quiz
print("Welcome to my computer quiz!")

# Ask the user if they want to play
playing = input("Do you want to play? (yes/no): ")

# If the user doesn't want to play, exit the program
if playing.lower() != "yes":
    print("Maybe next time!")
    quit()

# Let the user know the quiz is starting
print("Okay! Let's play :)")
score = 0  # Initialize score

# List of questions and answers
questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply unit"),
    ("What does SSD stand for? ", "solid state drive"),
    ("What does HDD stand for? ", "hard disk drive"),
    ("What does ROM stand for? ", "read-only memory"),
    ("What does USB stand for? ", "universal serial bus"),
]

# Shuffle the questions to make the quiz different each time
random.shuffle(questions)

total_questions = len(questions)  # Total number of questions

# Ask each question from the list
for question in questions:
    ask_question(*question)
    # Give the user the option to exit the quiz after each question
    if input("Press Enter to continue or type 'exit' to quit: ").lower() == "exit":
        print(f"Exiting the quiz. Your final score was {score}/{total_questions}.")
        quit()

# Final score message
print(f"You got {score} out of {total_questions} questions correct!")
percentage = (score / total_questions) * 100  # Calculate the percentage score
print(f"You scored {percentage:.2f}%.")

# Ask the user if they want to retry the quiz
retry = input("Do you want to retry the quiz? (yes/no): ")
if retry.lower() == "yes":
    # If yes, restart the quiz
    print("Restarting the quiz...")
    # Code to restart the quiz goes here
else:
    print("Thank you for playing!")
