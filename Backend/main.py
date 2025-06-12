import sys
import os

from fastapi import FastAPI
from pydantic import BaseModel

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Agent_AI_phoQtech.agents.task_classifier import TaskClassifier
from Agent_AI_phoQtech.agents.CalenderRequiredAgent import CalendarAgent
from Agent_AI_phoQtech.agents.subtask_generator import SubtaskGenerator
from Agent_AI_phoQtech.utils.prompt_builder import build_prompt
from Agent_AI_phoQtech.utils.json_storage import save_to_memory, load_from_memory

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

task_classifier = TaskClassifier()
calendar_agent = CalendarAgent()
subtask_generator = SubtaskGenerator()



@app.post("/plan")
async def process_task(request: TaskRequest):
    task = request.task

    needs_calendar = task_classifier.needs_calendar(task)
    calendar_events = calendar_agent.get_events() if needs_calendar else None
    prompt = build_prompt(task, calendar_events)
    subtasks = subtask_generator.get_subtasks(prompt)

    memory_data = load_from_memory()
    memory_data[task] = subtasks
    save_to_memory(memory_data)

    # return {
    #     "task": task,
    #     "needs_calendar": needs_calendar,
    #     "calendar_events": calendar_events or [],
    #     "subtasks": subtasks
    # }

    return {
        "success": True,
        "subtasks": subtasks
    }
