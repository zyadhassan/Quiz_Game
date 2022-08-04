class QuizBrain:
    def __init__(self, list_q):
        self.question_number = 0
        self.question_list = list_q
        self.score = 0

    def Still_Has_Question(self, FirstMistake=False):
        """ There Are two Modes of the Quiz
        First is to finish the quiz by First Mistake
        Put FirstMistake=True
        Second is to Finish the quiz by the end of Questions
        it's the Default Mode"""
        if FirstMistake:
            if self.score == self.question_number :
                return True
            else:
                return False
        else:
            if self.question_number < len(self.question_list):
                return True
            else:
                return False

    def next_question(self):
        text = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {text}  (True/False)? :")
        self.check_answer(user_answer=user_answer,correct_answer=answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You are right!")
        else:
            print("That is Wrong ")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your Current Score is : {self.score}/{self.question_number}\n")