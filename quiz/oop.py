from data import question_data
from question_model import Question
from brain import QuizBrain
question_bank=[]
for i in question_data:
    question=i['text']
    answer=i['answer']
    que=Question(question,answer)
    question_bank.append(que)
quiz=QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()
print(f"Your final score is {quiz.score}/{quiz.question_number}")