
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def create_quiz():
    questions = []
    num_questions = int(input("Enter the number of questions you want to add: "))
    for i in range(num_questions):
        prompt = input(f"Enter Question {i+1}: ")

        options = []
        for j in range(4):  # Assuming each question has 4 options
            option = input(f"Enter Option {j+1}: ")
            options.append(option)

        answer = input("Enter the correct answer (1-4): ")
        try:
            answer_index = int(answer) - 1
            if 0 <= answer_index < 4:
                answer = options[answer_index]
                question = Question(prompt, options, answer)
                questions.append(question)
            else:
                print("Invalid answer index! Please enter a valid option number (1-4).\n")
                return create_quiz()
        except ValueError:
            print("Invalid input! Please enter a valid option number (1-4).\n")
            return create_quiz()
    return questions

def take_quiz(questions):
    score = 0
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question.prompt}")
        for j, option in enumerate(question.options, start=1):
            print(f"{j}: {option}")
        user_answer = input("Your answer (1-4): ").strip()
        try:
            user_answer_index = int(user_answer) - 1
            if user_answer_index >= 0 and user_answer_index < 4:
                if question.options[user_answer_index] == question.answer:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.answer}\n")
            else:
                print("Invalid input! Please enter a valid option number (1-4).\n")
        except ValueError:
            print("Invalid input! Please enter a valid option number (1-4).\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

def main():
    questions = create_quiz()
    print("\nQuiz Starting...")
    take_quiz(questions)

if __name__ == "__main__":
    main()