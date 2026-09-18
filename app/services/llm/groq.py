from dotenv import load_dotenv
from langchain_groq import ChatGroq

from app.services.llm.base import LLMProvider


load_dotenv()


class GroqProvider(LLMProvider):

    def __init__(self):

        self.llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0
        )

    def generate(self, prompt: str) -> str:

        response = self.llm.invoke(prompt)

        return response.content