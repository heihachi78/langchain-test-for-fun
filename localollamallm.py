import requests
from langchain.llms.base import LLM

class LocalOllamaLLM(LLM):
    api_url: str
    model_name: str

    @property
    def _llm_type(self) -> str:
        return "local_ollama"

    def _call(self, prompt: str, stop: list = None) -> str:
        data = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }

        response = requests.post(f"{self.api_url}/api/chat", json=data)
        response.raise_for_status()

        result = response.json()
        #{
        # "model": "llama3.2",
        # "created_at": "2023-12-12T14:13:43.416799Z",
        # "message": {
        #   "role": "assistant",
        #   "content": "Hello! How are you today?"},
        # "done": true,
        # "total_duration": 5191566416,
        # "load_duration": 2154458,
        # "prompt_eval_count": 26,
        # "prompt_eval_duration": 383809000,
        # "eval_count": 298,
        # "eval_duration": 4799921000
        #}
        return result['message']['content']

    @property
    def _identifying_params(self) -> dict:
        """Get the identifying parameters."""
        return {"model_name": self.model_name}