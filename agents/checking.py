
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CalenderRequiredAgent import CalendarAgent
from subtask_generator import SubtaskGenerator
from task_classifier import TaskClassifier
from utils.prompt_builder import build_prompt

def test_agent_flow():
    task = "Plan my week"
    
    # Step 1: Check if calendar is needed
    classifier = TaskClassifier()
    needs_calendar = classifier.needs_calendar(task)
    print(f"Task requires calendar? {needs_calendar}")
    
    # Step 2: If yes, fetch calendar events
    calendar_events = []
    if needs_calendar:
        cal_agent = CalendarAgent()
        calendar_events = cal_agent.get_events()
        print(f"Fetched calendar events: {calendar_events}")
    
    # Step 3: Build prompt for subtask generator
    prompt = build_prompt(task, calendar_events if needs_calendar else None)
    print("Prompt to LLM:\n", prompt)
    
    # Step 4: Generate subtasks
    subtask_gen = SubtaskGenerator()
    subtasks = subtask_gen.get_subtasks(prompt)
    print("Generated subtasks:")
    for sub in subtasks:
        print("-", sub)

if __name__ == "__main__":
    test_agent_flow()