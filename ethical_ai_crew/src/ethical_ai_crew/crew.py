from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .agents import EthicalAIAgents
from .tasks import EthicalAITasks
from .tools.custom_tool import get_research_tools
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class EthicalAICrew():
    """EthicalAiCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    research_tools: List[str]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EthicalAiCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        # Initialize agents
        research_agent = self.agents[0]
        content_strategist_agent = self.agents[1]
        writing_agent = self.agents[2]
        editing_agent = self.agents[3]

        # Add tools to research agent
        research_agent.tools = self.research_tools

        # Create tasks
        research_task = self.tasks[0]
        outline_task = self.tasks[1]
        drafting_task = self.tasks[2]
        editing_task = self.tasks[3]

        # Create and return the crew
        return Crew(
            agents=[
                research_agent,
                content_strategist_agent,
                writing_agent,
                editing_agent
            ],
            tasks=[
                research_task,
                outline_task,
                drafting_task,
                editing_task
            ],
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

    def __init__(self):
        self.agents = EthicalAIAgents()
        self.tasks = EthicalAITasks()
        self.research_tools = get_research_tools()

    def create_crew(self):
        """
        Create and configure the Crew with all agents and tasks.
        """
        # Initialize agents
        research_agent = self.agents.create_research_agent()
        content_strategist_agent = self.agents.create_content_strategist_agent()
        writing_agent = self.agents.create_writing_agent()
        editing_agent = self.agents.create_editing_agent()

        # Add tools to research agent
        research_agent.tools = self.research_tools

        # Create tasks
        research_task = self.tasks.create_research_task(research_agent)
        outline_task = self.tasks.create_outline_task(content_strategist_agent, research_task)
        drafting_task = self.tasks.create_drafting_task(writing_agent, outline_task, research_task)
        editing_task = self.tasks.create_editing_task(editing_agent, drafting_task)

        # Create and return the crew
        return Crew(
            agents=[
                research_agent,
                content_strategist_agent,
                writing_agent,
                editing_agent
            ],
            tasks=[
                research_task,
                outline_task,
                drafting_task,
                editing_task
            ],
            verbose=True
        )
