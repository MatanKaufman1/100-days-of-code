import os
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self. question_list = q_list
        self.score = 0

    def still_has_quiestions(self):
        len_of_list = len(self.question_list)
        q_number = self.question_number

        return q_number < len_of_list

    def check_answer(self, user_answer, correct_answer):
        q_number = self.question_number
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")
            print(f"Your current score is: {self.score}/{q_number}")
            print("\n")
        else:
            print("You are wrong.")
            print(f"The correct answer is: {correct_answer}.")
            print(f"Your current score is: {self.score}/{q_number}")
            print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)