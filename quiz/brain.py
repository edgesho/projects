class QuizBrain:
    def __init__(self, que_list):
        self.question_number = 0
        self.question_list = que_list
        self.score=0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q.{self.question_number} {current_question.text} (True/False)?")
        self.check_answer(answer,current_question.answer)
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def check_answer(self,answer,current_answer):
        if answer.lower()==current_answer.lower():
            print("Correct answer.")
            self.score+=1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("Wrong answer.")
            print(f"Your current score is {self.score}/{self.question_number}")


