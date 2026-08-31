import os

from ollama import Client


class OllamaClient:
    """
    Local LLM client using Ollama.

    Ollama must be installed and running locally.

    Example .env:

        LLM_PROVIDER=ollama
        OLLAMA_HOST=http://localhost:11434
        OLLAMA_MODEL=qwen2.5:7b
    """

    def __init__(self):

        self.host = os.getenv(
            "OLLAMA_HOST",
            "http://localhost:11434"
        )

        self.model = os.getenv(
            "OLLAMA_MODEL",
            "qwen2.5:7b"
        )

        self.client = Client(
            host=self.host
        )

    def parse(
        self,
        instructions,
        input_text,
        response_model
    ):
        """
        Send a structured-output request to Ollama.

        response_model must be a Pydantic BaseModel class.
        """

        schema = response_model.model_json_schema()

        response = self.client.chat(

            model=self.model,

            messages=[
                {
                    "role": "system",
                    "content": instructions
                },
                {
                    "role": "user",
                    "content": input_text
                }
            ],

            format=schema,

            options={
                "temperature": 0
            }
        )

        content = response.message.content

        if not content:
            raise RuntimeError(
                "Ollama returned an empty response."
            )

        try:

            return response_model.model_validate_json(
                content
            )

        except Exception as exc:

            raise RuntimeError(
                "Ollama returned data that could not be "
                "validated against the expected schema.\n\n"
                f"Raw response:\n{content}"
            ) from exc