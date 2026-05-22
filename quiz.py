# Quiz Program

# List of questions, options, and answers
question = ("What is the capital of France?: ",
            "Which animal is known as the king of the jungle?: ",
            "What is the largest planet in our solar system?: ",
            "Who wrote the play 'Romeo and Juliet'?: ",
            "What is the chemical symbol for water?: ")

options = (("a) Paris", "b) London", "c) Rome", "d) Berlin"),
           ("a) Lion", "b) Tiger", "c) Elephant", "d) Giraffe"),
           ("a) Earth", "b) Jupiter", "c) Mars", "d) Saturn"),
           ("a) William Shakespeare", "b) Charles Dickens", "c) Mark Twain", "d) Jane Austen"),
           ("a) H2O", "b) CO2", "c) O2", "d) NaCl"))

answers = ("a", "a", "b", "a", "a")

# Initialize score and question number
score = 0 
question_number = 0

# Loop through each question and get user input
for x in question:
    print(x)
    for y in options[question_number]:
        print(y)
    user_answer = input("Enter your answer (a, b, c, or d): ")
    if user_answer.lower() == answers[question_number]:
        score = score + 1
        print("Correct!")
    else:
        print("Wrong!")
    question_number = question_number + 1

# Print the final score
print(f"Your final score is: {score}/{len(question)}")
