import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class OpenAIClient:
    """
    OpenAI LLM client.

    Example .env:

        LLM_PROVIDER=openai
        OPENAI_API_KEY=your_api_key
        OPENAI_MODEL=<available-model>
    """

    def __init__(self):

        self.api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if not self.api_key:

            raise RuntimeError(
                "OPENAI_API_KEY is not configured."
            )

        self.model = os.getenv(
            "OPENAI_MODEL"
        )

        if not self.model:

            raise RuntimeError(
                "OPENAI_MODEL is not configured."
            )

        self.client = OpenAI(
            api_key=self.api_key
        )

    def parse(
        self,
        instructions,
        input_text,
        response_model
    ):
        """
        Send a structured-output request to OpenAI.

        response_model must be a Pydantic BaseModel class.
        """

        response = self.client.responses.parse(

            model=self.model,

            instructions=instructions,

            input=input_text,

            text_format=response_model
        )

        parsed = response.output_parsed

        if parsed is None:

            raise RuntimeError(
                "OpenAI returned no structured output."
            )

        return parsed