import random

# Define the quiz questions and answers
quiz_questions = {
    "What is the capital of France?": ["Paris"],
    "How many planets are in the solar system?": ["8"],
    "What is the largest mammal?": ["Blue whale"],
    # Add more questions here
}

# Function to present the quiz questions
def present_quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(f"{question}\nYour answer: ")
        if user_answer.lower() in [a.lower() for a in answer]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {', '.join(answer)}")
    return score

# Main function to run the quiz game
def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions.")
    score = present_quiz(quiz_questions)
    print(f"Your final score is: {score}/{len(quiz_questions)}")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        quiz_game()
    else:
        print("Thanks for playing!")

# Run the quiz game
quiz_game()
