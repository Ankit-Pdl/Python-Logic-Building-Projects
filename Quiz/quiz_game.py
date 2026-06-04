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


