
# question ={
#     "1" : "Capital of France?"
# }
# answers = ["Paris"]
 #! major problem is question and answer are disconnected!


# for i in questions:
#     print(questions[i])
#     user_answer = input("Enter your answer:")
#     for i in range(len(answers)):
#         if user_answer == answers[i]:
#             print("[bold green]Great! Correct Answer![/bold green]")
        #    continue
        # else:
        #      print(f"[bold red]Ops wrong answer![/bold red]\ncorrect answer: [bold green]{answers[i]}[/bold green]")
        #     continue


from rich import print
import json
import random

with open("Quiz/questions.json","r") as file:
   questions = json.load(file)
score = 0

random.shuffle(questions)
questions= questions[:5]
for q in questions:
  print(q["question"])
  user_answer = input("Enter your answer:\n")
  if user_answer.strip().upper() == q["answer"].strip().upper():
   print("[bold green] Correct Answer![/bold green]")
   score +=1
  else:
   print(f"[bold red] Ops try again but in another question[/bold red]\nCorrect Answer:[bold green]{q['answer']}[/bold green]")

print(f"Your score is: {score}/{len(questions)}")  


