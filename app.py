from dash import dcc,html
import random
import dash
from dash.dependencies import Input, Output, State

# Define the questions and answers
questions = [
    "Is Python an interpreted language?",
    "Can you use Git to manage your code?",
    "Is Linux an operating system?",
    "Can you use Python for web development?",
    "Is Git a version control system?",
    "Can you use Linux for server administration?",
    "Is Python a low-level language?",
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
    "Can you use Git for continuous integration?",
    "Is Python a low-level language?",
    "Is Linux only used for servers and supercomputers?",
    "Does Linux have built-in support for networking and internet protocols?",
    "Is Linux known for its stability and security features?"
]

answers = [
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "yes",
    "no",
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
    "no",
    "no",
    "yes",
    "yes"
]

# Define the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Random Quiz"),
    html.H3(id="question"),
    dcc.Input(id="answer", type="text", placeholder="Enter your answer(yes/no)"),
    html.Button("Random Question", id="random-question-button", n_clicks=0),
    html.Button("Evaluate Answer", id="evaluate-answer-button", n_clicks=0),
    html.Div(id="answer-feedback")
])

# Define the callback to display a random question
@app.callback(Output("question", "children"), [Input("random-question-button", "n_clicks")])
def display_random_question(n_clicks):
    if n_clicks > 0:
        return(random.choice(questions))

# Define the callback to evaluate the answer
@app.callback(Output("answer-feedback", "children"),
              [Input("evaluate-answer-button", "n_clicks")],
              [State("answer", "value"), State("question", "children")])
def evaluate_answer(n_clicks, answer_value, question_value):
    if n_clicks > 0:
        expected_answer = answers[questions.index(question_value)]
        if answer_value == expected_answer:
            return html.Div("Correct!", style={"color": "green"})
        else:
            return html.Div("Incorrect.", style={"color": "red"})

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)

