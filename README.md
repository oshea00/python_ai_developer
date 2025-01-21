# CrewAI Agentic Example

This example code demonstrates an "Agentic" code generation and testing assistant.

I've adapted the basic code created by the ```crewai create crew <your name>``` command, powered by [crewAI](https://crewai.com) to my use case
of reading in a "programming_problem.txt" description then generating a solution using the agents and tasks defined in the `src/` folder.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

If you are proxying to ```api.openai.com``` or just wwant to use an openai compatible URL, you can set these in the .env as follows:
```
OPENAI_API_KEY=<yours>
OPENAI_BASE_URL=http://localhost:8088/v1 # your proxied url or remove this line to use openai's default location
OPENAI_MODEL_NAME=gpt-4o
OPENAI_MODEL_TEMPERATURE=0
OPENAI_MODEL_TOP_P=1
```

- Modify `src/python_ai_developer/config/agents.yaml` to define your agents
- Modify `src/python_ai_developer/config/tasks.yaml` to define your tasks
- Modify `src/python_ai_developer/crew.py` to add your own logic, tools and specific args
- Modify `src/python_ai_developer/main.py` to add custom inputs for your agents and tasks


## Running the Project

Note: **running in venv recommended**

* Update the ```programming_problem.txt``` file to describe the programming problem you want to solve.
* To initiate your crew of AI agents and begin task execution, run this from the root folder of your project:
```bash
$ crewai run
```
This command initializes the python-ai-developer Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create two files:
* `research_results.md` contains the research results and generated code.
* `test_results.md` file with the output of test results,

To extract python code from the ```research_results.md```
```bash
$ ./extract_code
```

After this, you should be able to run the `generated_code.py` as-is.
```
$ python generated_code.py
```

## Saving results
You can run `save_results <experiment_name>` to place the markdown and (if extracted), `generated_code.py` to a sub folder under `results`
for later analysis.


## Analyzing results
The included `nginx_log_processor.py` utility will extract the messages sent to openai during the crewai session.
```
$ python nginx_log_processor.py <path to exported docker logs output>
```
An example output from this is in `requests.txt`

## Proxying to OpenAI

In the `proxy_openai` folder there is a useful Docker container for setting up a local reverse proxy to ```api.openai.com```.
To build an run:
```bash
docker build -t rev-proxy .
docker run -d -p 8088:80 --name openai-proxy rev-proxy
docker logs openai-proxy -f
```

The logging will capture request body sent to ```api.openai.com``` for later analysis.







