# EthicalAiCrew Crew
This project showcases the design, development, and implementation of a sophisticated multi-agent AI system built with CrewAI. Our primary goal was to create an intelligent automation pipeline for generating high-quality, ethically-aware long-form content. As a tangible output, the system produced a comprehensive blog post titled, "Navigating the Ethical Maze: A Deep Dive into AI's Role in Content Creation."

Beyond the final content, this project meticulously documents the entire development journey, emphasizing iterative system design, advanced prompt engineering, and the critical role of a human-in-the-loop for quality assurance and ethical oversight. It demonstrates a practical approach to building robust AI applications that handle complex, nuanced topics with a focus on responsibility.

Welcome to the EthicalAiCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

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

- Modify `src/ethical_ai_crew/config/agents.yaml` to define your agents
- Modify `src/ethical_ai_crew/config/tasks.yaml` to define your tasks
- Modify `src/ethical_ai_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/ethical_ai_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the ethical_ai_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The ethical_ai_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the EthicalAiCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
