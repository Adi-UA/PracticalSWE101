# Define the quiz questions, options, and correct answers
quiz = [
    {
        "question": "What are the three main primitive data types in Python?",
        "options": [
            "A) Strings, Integers, Lists",
            "B) Integers, Floats, Booleans",
            "C) Tuples, Sets, Dictionaries",
            "D) Integers, Floats, Strings",
        ],
        "answer": "B",
    },
    {
        "question": "Which of the following is an example of an integer in Python?",
        "options": ["A) 10", "B) 3.14", "C) True", "D) 'Hello'"],
        "answer": "A",
    },
    {
        "question": "What operator would you use to perform integer division in Python?",
        "options": ["A) /", "B) //", "C) %", "D) **"],
        "answer": "B",
    },
    {
        "question": "What is the result of 10 / 3 in Python?",
        "options": ["A) 3", "B) 3.333...", "C) 10", "D) Error"],
        "answer": "B",
    },
    {
        "question": "Which operator would you use to multiply two numbers in Python?",
        "options": ["A) /", "B) *", "C) +", "D) %"],
        "answer": "B",
    },
    {
        "question": "What will the value of x be after running the following code?\nx = 5\nx += 3",
        "options": ["A) 8", "B) 5", "C) 3", "D) Error"],
        "answer": "A",
    },
    {
        "question": "What logical operator in Python represents 'and'?",
        "options": ["A) &", "B) &&", "C) and", "D) ||"],
        "answer": "C",
    },
    {
        "question": "Which of the following statements is true for Boolean data types in Python?",
        "options": [
            "A) They represent either True or False",
            "B) They can store numbers with decimal points",
            "C) They are a type of list",
            "D) They are used for string manipulations",
        ],
        "answer": "A",
    },
    {
        "question": "What does the following Python code return?\nbool(0)",
        "options": ["A) True", "B) False", "C) 0", "D) Error"],
        "answer": "B",
    },
    {
        "question": "In Python, what is the term used to describe the process of converting one data type to another?",
        "options": [
            "A) Type hinting",
            "B) Typecasting",
            "C) Typechecking",
            "D) Typing",
        ],
        "answer": "B",
    },
    {
        "question": "Which method would you use to concatenate two strings in Python?",
        "options": ["A) .concat()", "B) +", "C) .append()", "D) .join()"],
        "answer": "B",
    },
    {
        "question": "What will the following code output?\n'Hello' * 3",
        "options": ["A) HelloHelloHello", "B) Hello", "C) Error", "D) 3Hello"],
        "answer": "A",
    },
    {
        "question": "What is the purpose of using f-strings in Python?",
        "options": [
            "A) To create formatted strings easily",
            "B) To perform string concatenation",
            "C) To store multiple strings in a list",
            "D) To define a function",
        ],
        "answer": "A",
    },
    {
        "question": "What is an example of a valid variable name according to Python's naming conventions?",
        "options": ["A) myVariable", "B) 123var", "C) int", "D) def"],
        "answer": "A",
    },
    {
        "question": "Which of the following operators is used for exponentiation in Python?",
        "options": ["A) *", "B) **", "C) ^", "D) //"],
        "answer": "B",
    },
]


def run_quiz(quiz):
    score = 0
    user_answers = []

    # Print each question and get the user's answer
    for i, question in enumerate(quiz):
        print(f"Question {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        user_answers.append(answer)

        # Check if the answer is correct
        if answer == question["answer"]:
            score += 1
        print()

    # Show results at the end
    print("Quiz completed! Here are the correct answers:\n")
    for i, question in enumerate(quiz):
        print(f"Question {i + 1}: {question['question']}")
        print(f"Your answer: {user_answers[i]} | Correct answer: {question['answer']}")
        print()

    # Display final score
    print(f"Your total score: {score}/{len(quiz)}")


# Run the quiz
run_quiz(quiz)
