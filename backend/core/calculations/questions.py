questions = {
    "q1": {
        "image": "/static/practice/q1.png",
        "answers": [231.4, 16.67],
    },

    "q2": {
        "image": "/static/practice/q2.png",
        "answers": [160],
    },


}


import random

def get_random_question():
    key = random.choice(list(questions.keys()))
    return {"key": key, "image": questions[key]["image"], "numAnswers": len(questions[key]["answers"])}
