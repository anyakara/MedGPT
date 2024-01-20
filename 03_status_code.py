import requests
import json

# Replace these with your actual values
api_key = '{insert-api-key-here}'
training_file_id = '{insert-training-file-id}'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

data = {
    'training_file': training_file_id,
    'model': 'gpt-3.5-turbo-0613',
}

response = requests.post('https://api.openai.com/v1/fine_tuning/jobs', headers=headers, data=json.dumps(data))

# This will print the status code
print(response.json())