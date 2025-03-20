# First attempt at a quiz app using Python

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

# Defining the function to ask the questions

def ask_question():
    question = random.choice(list(questions.keys()))
    print(question)
    answer = input("Answer: ")
    if answer.lower() == questions[question].lower():
        print("Correct!")
    else:
        print("Incorrect! The correct answer is: ", questions[question])

# Defining the function to play the quiz

def play_quiz():
    print("Welcome to the Lesotho Quiz!")
    print("Answer the following questions to test your knowledge of Lesotho")
    print("Good luck!")

    while True:
        ask_question()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    print("Thank you for playing!")


# Calling the function to play the quiz
play_quiz()
