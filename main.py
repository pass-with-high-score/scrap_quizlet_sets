import requests
import json
import time

with open('flashcard.json', 'r') as file:
    data = json.load(file)

headers = {
    'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5ndXllbnF1YW5nbWluaDU3MEBnbWFpbC5jb20iLCJ1c2VySWQiOiI4Nzk3NTdmOS1hNjdjLTQwNmMtOGEwMC1hZWY3M2RhZjU3ZDkiLCJpYXQiOjE3MzA4ODE5NzIsImV4cCI6MTczMzQ3Mzk3Mn0.baZIZvugOD-w8BrHUyAYg4UJQgRiEC2unwzwDTqBukw',
    'Accept': '*/*',
    'Host': 'localhost:3009',
    'Connection': 'keep-alive'
}

count = 0
for entry in data:
    url = f"http://localhost:3009/study-set/import/{entry['userId']}"

    payload = json.dumps({
        "url": entry["link"]
    })

    response = requests.post(url, headers=headers, data=payload)

    print(f"Response for userId {entry['userId']}: {response.text}")

    count += 1
    if count == 10:
        print("Reached 10 requests, waiting for 60 seconds...")
        time.sleep(60)
        count = 0  # Reset count
