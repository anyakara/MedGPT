import csv
import json

def csv_to_jsonl(csv_file_path, jsonl_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    with open(jsonl_file_path, 'w') as jsonl_file:
        for i in range(0, 500):
        # for row in data:
            message = {
                "messages": [
                    {"role": "user", "content": data[i]["user"]},
                    {"role": "assistant", "content": data[i]["assistant"]}
                ]
            }
            jsonl_file.write(json.dumps(message) + '\n')

csv_to_jsonl('data.csv', 'output.jsonl')