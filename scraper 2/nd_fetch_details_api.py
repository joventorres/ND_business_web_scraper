import json
import csv
import requests
import time

# load companies_x.json that I got in Scraper 1: 'nd_scraper.py'
with open("companies_x.json", "r") as f:
    company_data = json.load(f)

companies = company_data.get("rows", {})
results = []

print(f"🔍 Now Fetching API details for {len(companies)} companies...\n")

for company_id, info in companies.items():
    name = info.get("TITLE", [""])[0]
    biz_id = info.get("ID", "")
    status = info.get("STATUS", "")

    if status != "Active":
        print(f"⚠️ Skipping {name} (not active)")
        continue

    url = f"https://firststop.sos.nd.gov/api/FilingDetail/business/{biz_id}/false"

    try:
        response = requests.get(url)
        data = response.json()

        details = data.get("DRAWER_DETAIL_LIST", [])

        commercial_agent = ""
        registered_agent = ""
        owner_name = ""

        for item in details:
            label = item.get("LABEL", "")
            value = item.get("VALUE", "")

            if label == "Commercial Registered Agent":
                commercial_agent = value.strip()
            elif label == "Registered Agent":
                registered_agent = value.strip()
            elif label == "Owner Name":
                owner_name = value.strip()

        results.append({
            "Company Name": name,
            "ID": biz_id,
            "Commercial Registered Agent": commercial_agent,
            "Registered Agent": registered_agent,
            "Owner Name": owner_name
        })

        print(f"✅ {name} – Success")

    except Exception as e:
        print(f"❌ Error with {name} (ID {biz_id}): {e}")

    time.sleep(1.5)

# JSON save
with open("companies_details_api.json", "w") as f:
    json.dump(results, f, indent=2)

# then Aave in CSV
with open("companies_details_api.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Company Name", "ID", "Commercial Registered Agent", "Registered Agent", "Owner Name"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("\n🎉 Done! Saved to:")
print("📁 companies_details_api.json")
print("📁 companies_details_api.csv")
