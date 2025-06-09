from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
leng=len(question_data)
print(leng)

question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_got_questions():
    quiz.next_question()
    
print(f"You've completed the quiz. Your final score was:{quiz.score}/{len(question_bank)}")
