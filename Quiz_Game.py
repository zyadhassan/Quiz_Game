from Data import question_data
from Question_Model import Question
from Quiz_Brain import QuizBrain

question_bank = []
for i in question_data:
    new_q = Question(i["text"], i["answer"])
    question_bank.append(new_q)

brain=QuizBrain(question_bank)
mode=input("There Are two Modes of the Quiz\n"
           "First is to finish the quiz by First Mistake\n"
           "Second is to Finish the quiz by the end of Questions\n"
           "Type (One or Two) :").lower()
if mode=='one':
    Mode_Game=True
else:
    Mode_Game=False

while brain.Still_Has_Question(Mode_Game):
    brain.next_question()
print("You have completed the Quiz")
print(f"Your Final score is {brain.score}/{len(question_bank)}")
