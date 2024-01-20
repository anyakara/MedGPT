# model inferences -- in the case we need to upload this information.
import requests

API_URL = "https://api-inference.huggingface.co/models/medicalai/ClinicalGPT-base-zh"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you be a clinical expert and answer my questions?",
})

print(output)