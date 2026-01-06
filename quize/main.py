# Python quize game

questions = {
    "'2' * 2 would result in" : "22",
    "is tuple data structure in python mutable y/n" : "n",
    "can we loop over a dictionary y/n" : "y",
    "is python a type strict language y/n" : "n",
    "can an int conver into a string in python y/n" : "y"
}

def play(quize:dict) -> int:
    score:int = 0
    for question,quize_answer in quize.items():
        print(question)
        answer = input("enter your answer: ").lower().strip()
        if answer != quize_answer:
            if score > 0:
               score -= 1
               print("wrong")
        else:
            score += 1
            print("right")
    return score
        

print(play(questions))