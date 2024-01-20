import requests
headers = {
    'Authorization': 'Bearer {insert-api-key}',
}

response = requests.get('https://api.openai.com/v1/fine_tuning/jobs/{id-of-fine-tuning}', headers=headers)

print(response.json())