import requests
import json
import csv

# Retrieve the JSON data from the API endpoint
response = requests.get('https://cxserver.wikimedia.org/v2/list/mt')
data = json.loads(response.text)

# Create a new CSV file and write the header row
with open('scraper.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['source language', 'target language', 'engine name'])

    # Loop through the JSON data and write each row to the CSV file
    for engine_name, languages in data.items():
     if engine_name == 'defaults':
                continue
    for source_language, target_languages in languages.items():
            for target_language in target_languages:
                writer.writerow([source_language, target_language, engine_name])
