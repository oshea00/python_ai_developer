import math  # Import the math library to use mathematical functions and constants


def main():
    print("Simple Math REPL (Read-Eval-Print Loop)")
    print("Type 'exit' to quit")
    print(
        "You can use basic math operations (+, -, *, /) and math functions/constants (e.g. math.sqrt, math.pi)"
    )

    while True:
        try:
            # Read user input
            expression = input("Enter expression: ")

            # Check exit condition
            if expression.strip().lower() == "exit":
                print("Exiting REPL. Goodbye!")
                break

            # Evaluate the expression while allowing usage of the math module
            # Use eval cautiously with provided context for safety
            # Only allow built-in functions and math module; no other built-ins
            allowed_names = {
                name: getattr(math, name)
                for name in dir(math)
                if not name.startswith("__")
            }
            allowed_names.update(
                {"abs": abs, "round": round}
            )  # Allow well-known safe built-ins

            # Evaluate the expression in a restricted namespace
            result = eval(expression, {"__builtins__": None}, allowed_names)

            # Print the result
            print("Result:", result)

        except Exception as e:
            # Catch any exceptions and print error message
            print("Error:", str(e))


if __name__ == "__main__":
    main()

# Explanation
# This code creates a simple REPL for mathematical operations using Python.
# - It imports the `math` module to access various mathematical functions and constants.
# - The loop continuously reads input expressions from the user until the user types 'exit'.
# - It safely evaluates mathematical expressions using `eval()` with a restricted set of built-in functions, limited to the math module and a few safe built-ins like `abs` and `round`.
# - Each result or error message is printed to provide feedback to the user immediately.

# Security:
# - Ensures only safe functions and constants are accessible to `eval()` by restricting the eval environment.
# - No direct access to dangerous built-ins or arbitrary code execution.
