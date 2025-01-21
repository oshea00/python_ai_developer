#!/usr/bin/env python
import sys
import warnings

from python_ai_developer.crew import PythonAiDeveloper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def load_problem():
    with open("programming_problem.txt", "r") as file:
        return file.read()


def run():
    """
    Run the crew.
    """
    inputs = {"topic": load_problem()}
    PythonAiDeveloper().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": load_problem()}
    try:
        PythonAiDeveloper().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PythonAiDeveloper().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": load_problem()}
    try:
        PythonAiDeveloper().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
