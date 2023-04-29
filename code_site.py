from flask import Flask, render_template, request
import random

app = Flask(__name__)

questions = [
    "Is Python an interpreted language?",
    "Can you use Git to manage your code?",
    "Is Linux an operating system?",
    "Can you use Python for web development?",
    "Is Git a version control system?",
    "Can you use Linux for server administration?",
    "Is Python a high-level language?",
    "Can you use Git to collaborate with others on code?",
    "Is Linux open-source software?",
    "Can you use Python for data analysis?",
    "Is Git commonly used in software development?",
    "Can you use Linux for cloud computing?",
    "Is Python an object-oriented language?",
    "Can you use Git to revert changes to code?",
    "Is Linux free to use?",
    "Can you use Python for machine learning?",
    "Is Git used for tracking changes to code?",
    "Can you use Linux for cybersecurity?",
    "Is Python easy to learn?",
    "Can you use Git for continuous integration?"
]

answers = [
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes"
]

@app.route('/')
def index():
    random_question_index = random.randint(0, 19)
    random_question = questions[random_question_index]
    return render_template('index.html', question=random_question)

@app.route('/', methods=['POST'])
def evaluate_answer():
    user_answer = request.form['answer']
    question_index = questions.index(request.form['question'])
    if user_answer.lower() == answers[question_index]:
        result = "Correct!"
    else:
        result = "Incorrect. The answer is {}".format(answers[question_index])
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
