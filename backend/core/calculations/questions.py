questions_unitConversion = {

    "q3": {
        "image": "/static/practice/q3.png",
        "answers": [2, 1.055, 74.57, 0.126, 2.03, 1.18, 120.701, 8896.44],
    },
    

    "q2": {
        "image": "/static/practice/q2.png",
        "answers": [160],
    },
}


questions_firstLaw = {

    "q1": {
        "image": "/static/practice/q1.png",
        "answers": [231.4, 16.67],
    },
}

questions_by_unit = {
    "unitConversion": questions_unitConversion,
    "firstLaw": questions_firstLaw,
}

import random

def get_random_question(unit: str):
    if unit not in questions_by_unit:
        return {"error": f"Unknown unit category: {unit}"}

    questions = questions_by_unit[unit]
    key = random.choice(list(questions.keys()))
    return {
        "id": key,
        "image": questions[key]["image"],
        "num_answers": len(questions[key]["answers"])
    }
