from openai import OpenAI

client = OpenAI()

task = input("What do you want me to do? ")

response = client.responses.create(
    model="gpt-5-mini",
    input=task
)

print("\nAI:", response.output_text)