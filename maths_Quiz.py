import random

# Defining The questions
def questions():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    operator=random.choice(['+','-','/','*','%','//'])
    match operator:
        case '+':
            answer=num1+num2
        case '-':
            answer=num1-num2
        case '/':
            answer=num1/num2
        case '*':
            answer=num1*num2
        case '%':
            answer=num1%num2
        case '//':
            answer=num1//num2
    return f"{num1} {operator} {num2}",answer

#Defining Score, rounds and remark criteria
def main_quiz():
    score=0
    rounds=5
    print("<-----Welcome to Python Maths Quiz---->")
    print("There will be total 5 rounds and each correct answer carry 1 score")
    
    for i in range(rounds):
        question,correct_answer=questions()
        print(f"Q{i+1}: {question}")
        if '/' in question:
            user_answer=float(input("Enter your answer upto 3 decimals:"))
        else:
            user_answer=int(input("Enter your answer:"))
        
        if round(user_answer,3)==round(correct_answer,3):
            print("Correct answer!!")
            score+=1
        else:
            print(f"Wrong answer!!. The Correct answer is: {correct_answer}")
    
    print("<----Game Over!--->")
    print(f"Your final score is: {score}/{rounds}")
    if score==rounds:
        print("Congratulation!!, your all answer is correct")
    elif score>=rounds//2:
        print("Keep it Up!, you are doing well.")
    else:
        print("Keep practicing! You can do better next time.")

# Quiz Run 
main_quiz()