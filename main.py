import requests
import json
import time

# Đọc dữ liệu từ file flashcard.json
with open('flashcard.json', 'r') as file:
    data = json.load(file)

# Headers chung cho tất cả các request
headers = {
    'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5ndXllbnF1YW5nbWluaDU3MEBnbWFpbC5jb20iLCJ1c2VySWQiOiI4Nzk3NTdmOS1hNjdjLTQwNmMtOGEwMC1hZWY3M2RhZjU3ZDkiLCJpYXQiOjE3MzA4ODE5NzIsImV4cCI6MTczMzQ3Mzk3Mn0.baZIZvugOD-w8BrHUyAYg4UJQgRiEC2unwzwDTqBukw',
    'Accept': '*/*',
    'Host': 'localhost:3009',
    'Connection': 'keep-alive'
}

# Lặp qua tất cả dữ liệu và gửi yêu cầu POST
count = 0
for entry in data:
    # Cập nhật URL với userId từ dữ liệu
    url = f"http://localhost:3009/study-set/import/{entry['userId']}"

    # Tạo payload với link
    payload = json.dumps({
        "url": entry["link"]
    })

    # Gửi request POST
    response = requests.post(url, headers=headers, data=payload)

    # In kết quả phản hồi
    print(f"Response for userId {entry['userId']}: {response.text}")

    # Tăng biến đếm và kiểm tra nếu đã gửi 10 yêu cầu
    count += 1
    if count == 10:
        # Dừng 60 giây sau khi đã gửi 10 yêu cầu
        print("Reached 10 requests, waiting for 60 seconds...")
        time.sleep(60)
        count = 0  # Reset count
