import requests
import os
from dotenv import load_dotenv

load_dotenv()

def bot(message: str, mail: str = "") -> dict:
	# Replace with your OpenRouter API key
	API_KEY: str = os.getenv('API_KEY_OPENROUTER')
	API_URL: str = 'https://openrouter.ai/api/v1/chat/completions'

	# Define the headers for the API request
	headers = {
		'Authorization': f'Bearer {API_KEY}',
		'Content-Type': 'application/json'
	}

	# Define the request payload (data)
	data = {
		"model": "deepseek/deepseek-chat:free",
		"messages": [{"role": "user", "content": "you are a person or society described here : " + message + " you have to answear in html this mail : " + mail}],
	}

	# Send the POST request to the DeepSeek API
	response = requests.post(API_URL, json=data, headers=headers)

	# Check if the request was successful
	if response.status_code == 200:
		r = response.json()
		if (r.get("choices")):
			r = r['choices'][0]['message']['content']
		return r
	else:
		print("Failed to fetch data from API. Status Code:", response.status_code)  
