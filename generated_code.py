import math
import argparse

def evaluate_expression(expression, variables):
    # Evaluate an expression with access to math functions and previous variables
    try:
        # Safely evaluate the expression using eval with limited global and local context
        result = eval(expression, {"__builtins__": None, "math": math}, variables)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"

def repl():
    print("Welcome to the Python Math REPL!")
    print("Type 'exit()' or 'quit()' to exit.")
    print("You can use basic math operations, store results in variables, and use math functions.")
    
    variables = {}
    
    while True:
        expression = input(">>> ")
        if expression.lower() in ['exit()', 'quit()']:
            break
        
        if "=" in expression:
            try:
                var, expr = [x.strip() for x in expression.split("=", 1)]
                result = evaluate_expression(expr, variables)
                variables[var] = result
                print(f"{var} = {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            result = evaluate_expression(expression, variables)
            print(result)


def main():
    parser = argparse.ArgumentParser(description='Simple Math REPL.')
    parser.add_argument('-c', '--calculate', help='Calculate expression and return result', type=str)
    args = parser.parse_args()
    
    if args.calculate:
        variables = {}
        result = evaluate_expression(args.calculate, variables)
        print(result)
    else:
        repl()

if __name__ == "__main__":
    main()
