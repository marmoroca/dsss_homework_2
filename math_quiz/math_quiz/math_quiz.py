#import the necessary libraries
import random


def create_random_number(min, max):
    """
    Random integer.
    
    This function creates a random integer between the given minimum and maximum values.

        min: The minimum integer value
        max: The maximum integer value

    It returns a random integer between `min` and `max'.
    """
    return random.randint(min, max)


def create_random_operator():
    """
    This function creates a random arithmetic operator   like (+, -, *).

    It returns a operator that was randomly selected.
    """
    return random.choice(['+', '-', '*'])


def solve_math_problem(n1, n2, o):
    """
    This function creates a math problem string and calculates the correct answer.

        n1: The first operand
        n2: The second operand
        o: The arithmetic operator
        p: problem 
        a: answer

    It returns a tuple containing the math problem string and the correct answer.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz_game():
    """
    This function is a math quiz, presenting the user with random arithmetic problems.

    The user is prompted to input their answers. The score is calculated based on correct answers.

        s: score
        t_q: total of questions 
        n1: number 1 
        n2: number 2
        o: operator 
    """
    s = 0
    t_q = 8 # You need to adjust the number of questions as needed 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = create_random_number(1, 10); n2 = create_random_number(1, 5); o = create_random_operator()

        PROBLEM, ANSWER = solve_math_problem(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        #Error handling  
        try: 
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz_game()