import requests

# Your AI21 Labs API key
API_KEY = 'av9hOuNvJJ6lVaEUt1qcOlrO0drP0R46'

def generate_response(prompt):
    url = "https://api.ai21.com/studio/v1/j2-light/complete"  # You can also use j2-medium, j2-large, j2-jumbo
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "numResults": 1,
        "maxTokens": 150,
        "temperature": 0.7,
        "topKReturn": 0,
        "topP":1
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['completions'][0]['data']['text'].strip()
    else:
        return "Sorry, I couldn't generate a response."

def chat():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
