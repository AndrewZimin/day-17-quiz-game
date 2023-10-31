class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        question_item = self.question_list
        question_text = question_item[self.question_number].text
        print("Please type your answer to the question")
        question_answer = input(f"{question_text}: ")
        self.question_number += 1

    def still_has_questions(self):
        return int(self.question_number) < len(self.question_list)


