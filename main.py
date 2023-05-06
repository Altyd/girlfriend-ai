import openai
import time

openai.api_key = "YOUR_API_KEY" #get api key here: https://openai.com/blog/openai-api

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Example conversation with a virtual girlfriend
while True:
    user_input = input("You: ")
    response = generate_response("Virtual girlfriend: " + user_input)
    print(response)
    time.sleep(1)
