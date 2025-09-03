from flask import Flask
import mathgenerator as mg

app = Flask(__name__)

@app.route("/")
def main():
    categories = ["algebra/basic"]
    response = ""
    for category in categories:
        line = f"<a href=\"/{category}/1\">{category}</a><br />"
        response += line
    return response

@app.route("/algebra/basic/<int:difficulty>")
def basic_algebra(difficulty):
    diff = 5
    if difficulty == 1:
        diff = 5
    elif difficulty == 2:
        diff = 20
    else:
        diff = 50
    problem, solution = mg.algebra.basic_algebra(diff)
    while True:
        if "/" in solution:
            problem, solution = mg.algebra.basic_algebra(diff)
        elif "0" in solution:
            problem, solution = mg.algebra.basic_algebra(diff)
        else:
            break

    data = {
        "problem": problem[1:-1],
        "solution": solution[1:-1]
    }
    return data

if __name__ == "__main__":
    app.run(debug=True)