from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question_record in question_data:
    question_bank.append(Question(question_record["text"], question_record["answer"]))

quiz = QuizBrain(question_bank)

quiz.next_question()
