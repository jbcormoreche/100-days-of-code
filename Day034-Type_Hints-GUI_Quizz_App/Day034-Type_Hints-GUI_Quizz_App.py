# Type Hints

# Type hints are used to indicate the type of a value.
# They help to spot some potential bugs.
# Colons are used for variables and arrows for functions (what type of value the function returns).
age: int
name: str
height: float
is_human: bool


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")

# Day 34 Project - GUI Quiz App
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
