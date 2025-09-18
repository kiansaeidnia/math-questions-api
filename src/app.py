from flask import Flask
import mathgenerator as mg

app = Flask(__name__)

@app.route("/")
def main():
    categories = [
            "algebra/basic",
            "algebra/combine_like_terms",
            "algebra/complex_quadratic",
            "algebra/factoring",
            "algebra/system_of_equations",
            "calculus/power_rule_differentiation",
            "calculus/power_rule_integration",
            "statistics/combinations",
            "statistics/permutations"
        ]
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
        "problem": problem,
        "solution": solution
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
        "problem": problem,
        "solution": solution
    }
    return data

@app.route('/algebra/complex_quadratic/<int:difficulty>')
def complex_quadratic(difficulty):
    diff = 5
    if difficulty == 1:
        diff = 5
    elif difficulty == 2:
        diff = 20
    else:
        diff = 30
    
    def generate():
        return mg.algebra.complex_quadratic(0, diff)
    
    problem, solution = generate()

    while True:
        if "\\sqrt" in solution:
            problem, solution = generate()
        else:
            break
        
    data = {
        "problem": problem,
        "solution": solution
    }
    return data

@app.route("/algebra/factoring/<int:difficulty>")
def expanding(difficulty):
    diff = 5
    if difficulty == 1:
        diff = 5
    elif difficulty == 2:
        diff = 20
    else:
        diff = 30

    def generate():
        return mg.algebra.factoring(diff, diff)
    
    problem, solution = generate()

    data = {
        "problem": problem,
        "solution": solution
    }

    return data

@app.route("/algebra/system_of_equations/<int:difficulty>")
def system_of_equations(difficulty):
    diff = 5
    if difficulty == 1:
        diff = 5
    elif difficulty == 2:
        diff = 20
    else:
        diff = 30

    def generate():
        return mg.algebra.system_of_equations(diff, diff, diff)
    
    problem, solution = generate()
    
    while True:
        if "/" in solution:
            problem, solution = generate()
        else:
            break

    data = {
        "problem": problem,
        "solution": solution
    }

    return data

# https://lukew3.github.io/mathgenerator/mathgenerator/calculus.html#power_rule_differentiation
@app.route("/calculus/power_rule_differentiation/<int:difficulty>")
def power_rule_differentiation(difficulty):
    max_coef = 5
    max_exp = 3
    max_terms = 1
    if difficulty == 1:
        max_coef = 5
        max_exp = 3
        max_terms = 1
    elif difficulty == 2:
        max_coef = 10
        max_exp = 5
        max_terms = 2
    else:
        max_coef = 15
        max_exp = 7
        max_terms = 3

    MAX_RETRIES = 10
    for _ in range(MAX_RETRIES):
        problem, solution = mg.calculus.power_rule_differentiation(max_coef, max_exp, max_terms)
        if "/" not in solution and "0" not in solution:
            break

    data = {
        "problem": problem,
        "solution": solution
    }
    return data

# https://lukew3.github.io/mathgenerator/mathgenerator/calculus.html#power_rule_integration
@app.route("/calculus/power_rule_integration/<int:difficulty>")
def power_rule_integration(difficulty):
    max_coef = 5
    max_exp = 3
    max_terms = 1
    if difficulty == 1:
        max_coef = 5
        max_exp = 3
        max_terms = 1
    elif difficulty == 2:
        max_coef = 10
        max_exp = 5
        max_terms = 2
    else:
        max_coef = 15
        max_exp = 7
        max_terms = 3

    MAX_RETRIES = 10
    for _ in range(MAX_RETRIES):
        problem, solution = mg.calculus.power_rule_integration(max_coef, max_exp, max_terms)
        if "/" not in solution and "0" not in solution:
            break

    data = {
        "problem": problem,
        "solution": solution
    }
    return data

# https://lukew3.github.io/mathgenerator/mathgenerator/statistics.html#combinations
@app.route("/statistics/combinations/<int:difficulty>")
def combinations_route(difficulty):
    # Map difficulty to max_lengthgth parameter
    if difficulty == 1:
        max_length = 5
    elif difficulty == 2:
        max_length = 7
    else:
        max_length = 10

    problem, solution = mg.statistics.combinations(10 + max_length)

    data = {
        "problem": problem,
        "solution": solution
    }
    return data

# https://lukew3.github.io/mathgenerator/mathgenerator/statistics.html#permutations
@app.route("/statistics/permutations/<int:difficulty>")
def permutations_route(difficulty):
    # Map difficulty to max_lengthgth parameter
    if difficulty == 1:
        max_length = 3
    elif difficulty == 2:
        max_length = 5
    else:
        max_length = 7

    problem, solution = mg.statistics.permutation(10 + max_length)

    data = {
        "problem": problem,
        "solution": solution
    }
    return data

if __name__ == "__main__":
    app.run(debug=True)