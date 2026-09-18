import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.7-flash"

client = genai.Client(api_key= API_KEY)


def generate_response(prompt : str):

    response = client.models.generate_content(
        model = MODEL_NAME,
        contents = prompt
    )
    return response