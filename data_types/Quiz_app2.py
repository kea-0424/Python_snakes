# Improved version of the Lesotho quiz app

# Importing the necessary modules
import random

# Defining the questions and answers
questions = {
    "Define Lesotho": "Lesotho is a landlocked country in South Africa",
    "What is the capital of Lesotho?": "Maseru",
    "When was Lesotho Founded?": "1824",
    "When did Lesotho become independent?": "1966",
    "What is the currency of Lesotho?": "Loti",
    "What is the official language of Lesotho?": "Sesotho",
    "Who is the current Prime Minister of Lesotho?": "Ntsokoane Sam Matekane",
    "What is the population of Lesotho?": "2.1 million",
    "Who is the founder of Lesotho?": "Moshoeshoe I",
    "What is the staple food of Basotho?": "Papa",
    "What is the nationality of Lesotho?": "Mosotho",
    "What is the national flower of Lesotho?": "Makhala",
    "What is the national symbol of Lesotho?": "Hat",
    "what animal is on the coat of arms of Lesotho?": "Crocodile",
    "what are the first five words on the national anthem of Lesotho?": "Lesotho Fatse La Bontata Rona",
    "When is Independence Day in Lesotho?": "4th October",
    "when is Moshoeshoe Day in Lesotho?": "11th March",
    "Who is the current King of Lesotho?": "Letsie III",
    "what colour is the flag of Lesotho?": "Blue, white, green and black",
    "what does each colour on the flag of Lesotho represent?": "Blue - sky, white - peace, green - prosperity",
}

def play_quiz():
    print("Welcome to the Lesotho Quiz!")
    print("Answer the following questions to test your knowledge of Lesotho")
    print("Good luck!")
    
    # Create a list of available questions to avoid repetition
    available_questions = list(questions.keys())
    
    # Initialize counters for correct and incorrect answers
    correct_count = 0
    incorrect_count = 0
    
    while available_questions and True:  # Continue as long as there are questions left
        # Select a random question from the available questions
        question = random.choice(available_questions)
        
        # Remove the question from available questions to avoid repetition
        available_questions.remove(question)
        
        # Ask the question
        print(question)
        answer = input("Answer: ")
        
        # Check if the answer is correct (case insensitive)
        if answer.lower() == questions[question].lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect! The correct answer is: {questions[question]}")
            incorrect_count += 1
        
        # Display current score
        total_answered = correct_count + incorrect_count
        print(f"Score: {correct_count}/{total_answered} ({correct_count/total_answered*100:.1f}%)")
        
        # Check if there are any questions left
        if not available_questions:
            print("\nYou've answered all the questions!")
            print(f"Final score: {correct_count}/{total_answered} ({correct_count/total_answered*100:.1f}%)")
            break
        
        # Ask if the user wants to continue
        play_again = input("Do you want to continue? (yes/no): ")
        if play_again.lower() != "yes":
            # Show the final score before exiting
            print(f"\nFinal score: {correct_count}/{total_answered} ({correct_count/total_answered*100:.1f}%)")
            break
    
    print("Thank you for playing!")

# Call the function to play the quiz
if __name__ == "__main__":
    play_quiz()
    