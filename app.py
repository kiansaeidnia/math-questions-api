from flask import Flask
import mathgenerator as mg

app = Flask(__name__)

@app.route("/")
def main():
    categories = ["algebra/basic", "algebra/combine_like_terms"]
    response = ""
    for category in categories:
        line = f"<a href=\"/{category}/1\">{category}</a><br />"
        response += line
    return response

# https://lukew3.github.io/mathgenerator/mathgenerator/algebra.html#basic_algebra
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

# https://lukew3.github.io/mathgenerator/mathgenerator/algebra.html#combine_like_terms
@app.route('/algebra/combine_like_terms/<int:difficulty>')
def combine_like_terms(difficulty):
    diff = 5
    if difficulty == 1:
        diff = 5
    elif difficulty == 2:
        diff = 20
    else:
        diff = 30

    def generate():
        return mg.algebra.combine_like_terms(diff, round(diff*2), round(diff/3) if diff > 5 else round(diff/2) )

    problem, solution = generate()
    while True:
        if "/" in solution:
            problem, solution = generate()
        elif "0" in solution:
            problem, solution = generate()
        elif "+" not in solution:
            problem, solution = generate()
        else:
            break

    data = {
        "problem": problem[1:-1],
        "solution": solution[1:-1]
    }
    return data


if __name__ == "__main__":
    app.run(debug=True)