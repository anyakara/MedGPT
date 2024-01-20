import openai

openai.api_key = '{insert-api-key}'

response2 = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo:{my_org_name}:{model_name}:{model_id}",
  messages=[
        {"role": "system", "content": "You are a health assistant."},
        {"role": "user", "content": "What causes Gastritis?"},
        {"role": "user", "content": "My head is hurting after running too long, why?"},
    ]
)

print(response2['choices'][0])