from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["question"]
    questions_answer = q["correct_answer"]
    new_question = Questions(question_text, questions_answer)
    question_bank.append(new_question) 

quiz = QuizBrain(question_bank)
while quiz.still_has_quiestions():
    quiz.next_question()

print(f"You completed the quiz")
print(f"Your final score was:{quiz.score}/{len(question_bank)}")