from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool
from pydantic import BaseModel


class Code(BaseModel):
    description: str
    type: str
    source_code: str


class Libraries(BaseModel):
    description: str
    type: list[str]


class CodeOutput(BaseModel):
    code: Code
    libraries_used: Libraries


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class PythonAiDeveloper:
    """PythonAiDeveloper crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def code_researcher(self) -> Agent:
        return Agent(config=self.agents_config["code_researcher"], verbose=True)

    @agent
    def code_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["code_writer"],
            verbose=True,
            allow_code_generation=True,
        )

    @agent
    def code_tester(self) -> Agent:
        tools = []
        tools.append(CodeInterpreterTool())
        return Agent(
            config=self.agents_config["code_tester"],
            verbose=True,
            tools=tools,
            allow_code_execution=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def write_code_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_code_task"],
            output_file="generated_code.py",
        )

    @task
    def test_code_task(self) -> Task:
        return Task(
            config=self.tasks_config["test_code_task"], output_file="test_results.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PythonAiDeveloper crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
