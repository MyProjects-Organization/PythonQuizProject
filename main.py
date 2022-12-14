from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
#
question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# print(question_bank)
# print(question_bank[0].text)

quiz = QuizBrain(question_bank)
# This line: "print(quiz)" will output <quiz_brain.QuizBrain object at 0x7f9a9fce2070>
print(quiz)
# This line: "quiz.next_question()" will output Q. 1: A slug's blood is green. (True/False)?
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()


# for i in range(0,4):
#     # print(random.randint(0,11))
#     rand = random.randint(0,11)
#     print(question_bank[rand].text, question_bank[rand].answer)

# list = [20, 30, 40, 50 ,60, 70, 80]
# sampling = random.choices(list, k=4)
# print("Randomly selected multiple choices using random.choices() ", sampling)
