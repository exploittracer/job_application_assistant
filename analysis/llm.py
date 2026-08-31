import os

from dotenv import load_dotenv


load_dotenv()


class LLMClient:
    """
    Provider-independent LLM client.

    Supported providers:
        - ollama
        - openai

    Configure through .env:

        LLM_PROVIDER=ollama
        OLLAMA_MODEL=qwen2.5:7b

    or:

        LLM_PROVIDER=openai
        OPENAI_MODEL=<your-model>
    """

    def __init__(self):

        self.provider = os.getenv(
            "LLM_PROVIDER",
            "ollama"
        ).lower()

        if self.provider == "ollama":

            from analysis.ollama_client import OllamaClient

            self.client = OllamaClient()

        elif self.provider == "openai":

            from analysis.openai_client import OpenAIClient

            self.client = OpenAIClient()

        else:

            raise ValueError(
                f"Unsupported LLM provider: {self.provider}. "
                "Use 'ollama' or 'openai'."
            )

        self.model = self.client.model

    def parse(
        self,
        instructions,
        input_text,
        response_model
    ):
        """
        Send a request to the configured LLM provider and return
        a validated Pydantic model.
        """

        return self.client.parse(
            instructions=instructions,
            input_text=input_text,
            response_model=response_model
        )