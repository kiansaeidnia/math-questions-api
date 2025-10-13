import random


def basic_algebra(difficulty):
  """
  Generates a simple linear algebra problem (ax + b = c)
  with a guaranteed whole number solution.

  Returns:
      tuple: A tuple containing the problem string and the integer solution
             in the format (problem, solution).
  """
  # 1. First, pick a whole number for the solution 'x'
  solution = random.randint(1, round(difficulty / 3))
  
  # 2. Pick random integers for the other parts of the equation
  a = random.randint(2, round(difficulty / 2)) # Coefficient for x
  b = random.randint(1, difficulty) # Constant to add
  
  # 3. Calculate the result 'c' based on the chosen solution
  c = a * solution + b
  
  # 4. Format the problem into a user-friendly string
  problem_string = f"{a}x + {b} = {c}"
  
  # 5. Return the result as a tuple
  return (problem_string, str(solution))

def factoring_problem(difficulty):
    """
    Generates a factorable quadratic equation (x^2 + bx + c = 0).

    Returns:
        dict: A dictionary containing the problem and a solution object.
    """
    # 1. Choose two distinct, non-zero integer roots for the equation.
    root1 = random.choice([i for i in range(-10, round(difficulty / 2)) if i != 0])
    root2 = random.choice([i for i in range(-10, round(difficulty /2) ) if i != 0 and i != root1])

    # 2. Calculate coefficients b and c from the roots.
    # From the form (x - root1)(x - root2) = x^2 - (root1 + root2)x + (root1 * root2)
    b = -(root1 + root2)
    c = root1 * root2

    # 3. Format the problem string with proper signs.
    # Handle the 'b' coefficient (the x term)
    if b == 1:
        b_str = " + x"
    elif b == -1:
        b_str = " - x"
    elif b > 0:
        b_str = f" + {b}x"
    elif b < 0:
        b_str = f" - {abs(b)}x"
    else: # b is 0
        b_str = ""

    # Handle the 'c' coefficient (the constant term)
    if c > 0:
        c_str = f" + {c}"
    else: # c is negative
        c_str = f" - {abs(c)}"

    problem = f"x^{{2}}{b_str}{c_str} = 0"

    # 4. Format the solution string and the list of roots.
    def format_factor(r):
        num = -r
        return f"(x + {num})" if num > 0 else f"(x - {abs(num)})"

    factored_form = f"{format_factor(root1)}{format_factor(root2)}"
    
    # solution = {
    #     "factored_form": factored_form,
    #     "roots": sorted([root1, root2]) # The values of x that solve the equation
    # }

    return (problem, factored_form)

def power_rule_differentiation(difficulty):
    
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

    numTerms = random.randint(1, max_terms)

    problem = ""
    solution = ""
    
    for i in range(numTerms):

        if i > 0:

            problem += " + "

            solution += " + "

        coefficient = random.randint(1, max_coef)

        exponent = random.randint(1, max_exp)


        problem += f'{coefficient}x^{{{exponent}}}'

        solution += f'{coefficient * exponent}x{"^" + str(exponent - 1) if exponent > 2 else ""}'


    return (problem, solution)