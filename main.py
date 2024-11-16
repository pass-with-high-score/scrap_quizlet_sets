import requests
import json
import time

# Load data from the flashcard JSON file
with open('flashcard.json', 'r') as file:
    data = json.load(file)

# Initialize the failed requests list (if it exists, load it)
try:
    with open('failed_requests.json', 'r') as failed_file:
        failed_requests = json.load(failed_file)
except FileNotFoundError:
    failed_requests = []

headers = {
    'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5ndXllbnF1YW5nbWluaDU3MEBnbWFpbC5jb20iLCJ1c2VySWQiOiI4Nzk3NTdmOS1hNjdjLTQwNmMtOGEwMC1hZWY3M2RhZjU3ZDkiLCJpYXQiOjE3MzA4ODE5NzIsImV4cCI6MTczMzQ3Mzk3Mn0.baZIZvugOD-w8BrHUyAYg4UJQgRiEC2unwzwDTqBukw',
    'Accept': '*/*',
    'Host': 'localhost:3009',
    'Connection': 'keep-alive'
}

count = 0
successful_requests = []  # List to store successful requests

# Loop through each entry in the data
while data or failed_requests:  # Run until both lists are empty
    if not data and failed_requests:
        print("Retrying failed requests...")

    for entry in (data[:] + failed_requests[:]):  # Iterate over current data and failed requests
        url = f"http://localhost:3009/study-set/import/{entry['userId']}"

        payload = json.dumps({
            "url": entry["link"]
        })

        # Send the POST request
        response = requests.post(url, headers=headers, data=payload)

        # Print out detailed information about the request
        print(f"Sending request for userId: {entry['userId']}")
        print(f"Link: {entry['link']}")
        print(f"Response: {response.status_code} - {response.text}")

        # If the request is successful, mark it as successful and remove from the list
        if response.status_code == 200:  # You can adjust the success condition based on your API
            successful_requests.append(entry)
            if entry in data:
                data.remove(entry)  # Remove the entry from the data list after successful request
            elif entry in failed_requests:
                failed_requests.remove(entry)  # Remove from failed requests if it's in that list

        else:
            # If the request fails, add it to the failed_requests list (if not already present)
            if entry not in failed_requests:
                failed_requests.append(entry)

        count += 1

        # If 10 requests have been made, wait for 60 seconds before continuing
        if count == 10:
            print("Reached 10 requests, waiting for 60 seconds...")
            time.sleep(60)
            count = 0  # Reset the counter after the wait

    # After processing, save failed requests to a file
    with open('failed_requests.json', 'w') as failed_file:
        json.dump(failed_requests, failed_file, indent=4)

# Save the remaining data back to the JSON file after processing
with open('flashcard.json', 'w') as file:
    json.dump(data, file, indent=4)

# Print a summary of successful requests
print("\nSummary of successful requests:")
for success in successful_requests:
    print(f"User ID: {success['userId']} | Link: {success['link']}")

# Print failed requests
if failed_requests:
    print("\nRetrying some failed requests:")
    for failed in failed_requests:
        print(f"User ID: {failed['userId']} | Link: {failed['link']}")
else:
    print("\nAll requests were successful.")
