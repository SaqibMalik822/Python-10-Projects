import time as t
import random as rd

def generate_question(operant:str) -> tuple[int, int]:
    rndm_1 = rd.randrange(1,1000)
    rndm_2 = rd.randrange(1,1000)
    return rndm_1, rndm_2

def generate_answer(gr_rndm) -> tuple[int, str]:
    user_input = input("enter the operant: ")
    (rndm_1,rndm_2) = gr_rndm(user_input)
    if(user_input not in ("-","+","/","*")):
        return "enter a valid operant"
    elif user_input == "-":
        question = f"{rndm_1} - {rndm_2}"
        return rndm_1 - rndm_2,  question
    elif user_input == "+":
        question = f"{rndm_1} + {rndm_2}"
        return rndm_1 + rndm_2, question
    elif user_input == "/":
        question = f"{rndm_1} / {rndm_2}"
        return rndm_1 / rndm_2, question
    elif user_input == "*":
        question = f"{rndm_1} * {rndm_2}"
        return rndm_1 * rndm_2, question

def play(gr_rndm, gr_answer) -> str:
    (answer, question) = gr_answer(gr_rndm)
    while True:
        print(question)
        start = t.perf_counter()
        user_answer = input("enter your answer: ")
        try:
            user_answer = int(user_answer)
        except ValueError:
            return "enter a number next time"
        if(user_answer == answer):
            end = t.perf_counter()
            difference = end - start
            return f"you answered the question correctly in {round(difference,2)} seconds"
        else:
            continue        

print(play(generate_question,generate_answer))