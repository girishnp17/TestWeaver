from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, DirectoryReadTool, CodeInterpreterTool, FileWriterTool
from typing import List
import os

# Commented out OpenRouter API configuration
# openrouter_llm = LLM(
#     model="openrouter/deepseek/deepseek-chat",
#     base_url="https://openrouter.ai/api/v1",
#     api_key="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",
#     temperature=0.1
# )

# Configure vLLM endpoint using CrewAI's LLM class
# Set environment variables for the OpenAI-compatible endpoint
os.environ["OPENAI_API_BASE"] = "http://Girish-Qwen:8000/v1"
os.environ["OPENAI_API_KEY"] = "dummy"

vllm_llm = LLM(
    model="openai/Qwen/Qwen2.5-Coder-7B-Instruct",
    base_url="http://Girish-Qwen:8000/v1",
    api_key="dummy",
    temperature=0.1,
    timeout=1200
)

@CrewBase
class Tester:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def code_analyzer(self) -> Agent:
        config = self.agents_config['code_analyzer']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            llm=vllm_llm,
            verbose=config.get('verbose', True)
        )

    @agent
    def test_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['test_strategist'],
            llm=vllm_llm,
            verbose=True
        )

    @agent
    def test_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['test_generator'],
            tools=[FileWriterTool()],
            llm=vllm_llm,
            verbose=True
        )

    @agent
    def test_executor(self) -> Agent:
        return Agent(
            config=self.agents_config['test_executor'],
            tools=[FileReadTool(), DirectoryReadTool()],
            allow_code_execution=True,
            llm=vllm_llm,
            verbose=True
        )

    @agent
    def quality_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_reviewer'],
            tools=[FileReadTool(), DirectoryReadTool()],
            llm=vllm_llm,
            verbose=True
        )
    
    @task
    def analyze_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_code_task'],
        )
    
    @task
    def design_test_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_test_strategy_task'],
        )
    
    @task
    def generate_test_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_test_code_task'],
        )

    @task
    def execute_tests_task(self) -> Task:
        return Task(
            config=self.tasks_config['execute_tests_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )