from openai import AzureOpenAI
import os
import requests
import json

client = AzureOpenAI(

	api_key = os.getenv("AZURE_KEY"),
	azure_endpoint = os.getenv("AZURE_ENDPOINT"),
	api_version = "2023-10-01-preview"
	)

messages = [
    {"role": "system", "content": "Respond to everything as a short poem."},
    {"role": "user", "content": "Find the latest cats news."}
]

def get_cat_fact():
    url = 'https://cat-fact.herokuapp.com/facts/random'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['text']
    else:
        return "Error fetching cat fact."


def generate_openai_response(user_question, cat_fact):
    functions = [
        {"role": "system", "content": "You are a cat who loves to share fun and interesting facts about cats. Answer everything from a cat's perspective."},
        {"role": "user", "content": user_question},
        {"role": "system", "content": f"Here's an interesting cat fact: {cat_fact}. Now, answer the user question with that in mind!"}
    ]
    
    
    response = client.chat.completions.create(
        model="GPT-4",
        messages=functions
    )
    return response


while True:
    
    user_question = input("Ask me anything about cats (or type 'exit' to quit): ")

    
    if user_question.lower() == 'exit':
        print("Goodbye! See you next time!")
        break
    
    
    cat_fact = get_cat_fact()

    
    response = generate_openai_response(user_question, cat_fact)

    
    print(f"\n(=①ω①=): {(response.choices[0].message.content)}")