To solve the described problem of creating a REPL (Read-Eval-Print Loop) for simple math operations, we can use Python's capabilities to parse and evaluate expressions dynamically, handle user input, and provide a command-line interface with options. Below is a detailed breakdown of the relevant libraries, algorithms, and techniques, followed by the complete implementation in Python.

### Libraries and Techniques:
1. **Built-in `math` Library**: 
   - This library provides access to mathematical functions like `sin`, `cos`, `tan`, and constants such as `pi` and `e`.
   - Importing `math` will allow use of these functions and constants in user expressions.

2. **AST (Abstract Syntax Trees) and `eval`**:
   - We can use Python's `eval()` function to dynamically evaluate expressions entered by the user.
   - To ensure safety (only evaluate safe expressions), you might use `ast` to parse and inspect the expression tree.

3. **Command-Line Parsing**:
   - Use Python's `argparse` to handle command-line arguments including the `-c` option for expressions.
   - Enables users to provide initial calculations on the command line and exit after evaluation.

4. **Dictionary for Variable Storage**:
   - Use a Python dictionary to store results of calculations which can be referenced later.

5. **Loop and Input Handling**:
   - A simple infinite loop (`while True`) for the REPL, with condition to break out when the user types an exit command like `exit()` or `quit()`.

### Implementation:

```python
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
```

### Explanation:

- **`evaluate_expression`:** Safely evaluates the user-provided expression, allowing usage of math functions and accessing stored variables.
- **REPL Implementation:** Starts with a welcome message and a loop to continually accept input. Handles assignment with the `=` operator and evaluates expressions using mathematical and stored variable context.
- **Command-Line Interface with `-c`:** Uses `argparse` to handle a command-line expression if provided. The program will exit after evaluating this expression.
- **Variable Storage:** Maintains a dictionary `variables` for storing and referencing previous results.

This Python script captures all the requirements and allows for a flexible and comprehensive REPL for simple math operations with the additional capability of executing a standalone calculation from the command line.