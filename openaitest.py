import openai
from api_key import api_key

# Set your OpenAI API key
openai.api_key = api_key

# Function to interact with the ChatGPT model
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
