import requests
import json

url = "https://firststop.sos.nd.gov/api/Records/businesssearch"
payload = {
    "SEARCH_VALUE": "X",
    "STARTS_WITH_YN": True,
    "STATUS": "Active"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    with open("companies_x.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved {len(data)} companies to companies_x.json")
else:
    print("❌ Failed to fetch data.")
    print("Status:", response.status_code)
    print("Response:", response.text)
