from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class PythonAiDeveloper:
    """PythonAiDeveloper crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def code_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["code_researcher"],
            verbose=True,
        )

    @agent
    def code_tester(self) -> Agent:
        return Agent(
            config=self.agents_config["code_tester"],
            verbose=True,
            allow_code_execution=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"], output_file="research_results.md"
        )

    @task
    def test_code_task(self) -> Task:
        return Task(
            config=self.tasks_config["test_code_task"], output_file="test_results.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PythonAiDeveloper crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
