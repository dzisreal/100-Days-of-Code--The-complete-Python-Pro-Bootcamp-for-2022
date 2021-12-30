from question_model import question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    i_text = i["text"]
    i_answer = i["answer"]
    new_question = question(i_text,i_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("\n")
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}.")

