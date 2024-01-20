import requests

api_key = ''
file_path = r'output.jsonl'

headers = {
    'Authorization': f'Bearer {api_key}',
}

data = {
    'purpose': 'fine-tune',
}

files = {
    'file': open(file_path, 'rb'),
}

response = requests.post('https://api.openai.com/v1/files', headers=headers, data=data, files=files)

# This will print the status code
print(response.status_code)
print(response.json())