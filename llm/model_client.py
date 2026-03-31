import ollama

class ModelClient:
    def __init__(self, model="mistral"):
        self.model = model

    def chat(self, system_prompt: str, user_message: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_message},
            ]
        )
        return response["message"]["content"]