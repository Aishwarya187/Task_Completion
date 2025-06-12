import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
HF_MODEL = "gpt2"  # Or any other text-generation model on HF

class SubtaskGenerator:
    def __init__(self):
        self.api_url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
        self.headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

    def get_subtasks(self, prompt):
        # You can prepend system prompt manually here
        full_prompt = (
            "You are an assistant that breaks down tasks into subtasks.\n"
            f"Task: {prompt}\n"
            "List the subtasks clearly as bullet points.\n"
        )
        payload = {
            "inputs": full_prompt,
            "parameters": {
                "max_new_tokens": 100,
                "temperature": 0.7,
                "return_full_text": False
            }
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)
        response.raise_for_status()
        result = response.json()

        # result is a list of dicts with 'generated_text' key
        generated_text = result[0]['generated_text']

        # Extract bullet points or lines starting with '-'
        subtasks = [line.strip("- \n") for line in generated_text.split("\n") if line.strip()]
        return subtasks