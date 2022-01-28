# Benefits of Object Oriented Programming

# Break a program into solvable bit-sized problems that can be solved one at a time
# Modular and flexible by building modules that communicate with one another
# Each bit of functionality does its own thing
# Work on multiple objects simultaneously
# Multiple instances of objects can co-exist without any interference
# Reuse code to save time
# Intuitive approach for developing big projects
# Upgradable from small to large systems
# Better productivity, better quality of software and lesser maintenance cost
# Easy troubleshooting

# Create an empty Class
class User:
    pass


# Create a new object from a Class
user_1 = User()

# Create an attribute (variable associated with an object) from a Class
user_1.id = "001"
user_1.username = "James"

print(user_1.username)


# Create a constructor, used to initialize the starting values of an attribute
class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Add a method to a Class
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "James")
user_2 = User("002", "Jack")
print(user_1.id, user_1.username, user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Day 17 Project - Quiz
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
