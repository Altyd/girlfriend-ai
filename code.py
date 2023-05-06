import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

prompt = "Create a virtual girlfriend for me."
generated_text = generate_text(prompt)
print(generated_text)
