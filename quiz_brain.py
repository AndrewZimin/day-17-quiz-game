class QuizBrain:

    user_score = 0
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        question_item = self.question_list
        question_text = question_item[self.question_number].text
        question_answer = question_item[self.question_number].answer
        print("Please type your answer to the question")
        user_answer = input(f"{question_text}: ")
        self.question_number += 1
        self.check_answer(user_answer=user_answer, correct_answer=question_answer)

    def still_has_questions(self):
        return int(self.question_number) < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.user_score += 1
        else:
            print(f"Wrong... It's {correct_answer}" )
        print(f"Your score is {self.user_score}/{self.question_number}")