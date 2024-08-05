import models.openai as openai
from model_services import Model

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'


class OpenAI(Model):

    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt, engine="text-davinci-003", max_tokens=150, temperature=0.7):
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )
        return response.choices[0].text.strip()